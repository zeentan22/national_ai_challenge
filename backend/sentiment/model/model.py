from sgnlp.models.sentic_gcn import(
    SenticGCNBertConfig,
    SenticGCNBertModel,
    SenticGCNBertEmbeddingConfig,
    SenticGCNBertEmbeddingModel,
    SenticGCNBertTokenizer,
    SenticGCNBertPreprocessor,
    SenticGCNBertPostprocessor
)

from rake_nltk import Rake
import nltk 
nltk.download('stopwords')


class AspectExtraction:
    def __init__(self):
        self.model = Rake()

    def get_aspect(self, input: str) -> str:
        self.model.extract_keywords_from_text(input) 
        return self.model.get_ranked_phrases()[0]

class NLPModel:
    def __init__(self, *inputs: dict):

        #import os
        #print(os.getcwd())
        #while True:
        #    pass

        tokenizer = SenticGCNBertTokenizer.from_pretrained("bert-base-uncased")

        config = SenticGCNBertConfig.from_pretrained(
            "./sentiment/model/senticgcnbert/config.json")
        self.model = SenticGCNBertModel.from_pretrained(
            "./sentiment/model/senticgcnbert/pytorch_model.bin",
            config=config
        )
        embed_config = SenticGCNBertEmbeddingConfig.from_pretrained("bert-base-uncased")

        embed_model = SenticGCNBertEmbeddingModel.from_pretrained("bert-base-uncased",
            config=embed_config
        )
        self.preprocessor = SenticGCNBertPreprocessor(
            tokenizer=tokenizer, embedding_model=embed_model,
            senticnet="./sentiment/model/senticNet/senticnet.pickle",
            device="cpu")

        self.postprocessor = SenticGCNBertPostprocessor()

        self.inputs = None
        self.output = None

    def __repr__(self):
        print("hello")
        print(self.output)
        rep = f"Model output is {self.output}"
        return rep

    def set_input(self, *inputs):
        # aspect extraction
        aspect_extractor = AspectExtraction()
        for input in inputs:
            input["aspects"] = [aspect_extractor.get_aspect(input["sentence"])]
        self.inputs = inputs
        return self

    def run(self):
        processed_inputs, processed_indices = self.preprocessor(self.inputs)
        raw_outputs = self.model(processed_indices)
        post_outputs = self.postprocessor(processed_inputs=processed_inputs, model_outputs=raw_outputs)
        self.output = post_outputs
    
    """ getting the whole item in this format {'sentence': [], 'aspects': [[1]], 'labels':[1]}"""
    def get(self, index):
        return self.output[index]
    
    """ getting one aspect only """

    def get_aspect(self, index = 0):
        item = self.output[index]
        sentence = item["sentence"]
        aspect_index = item['aspects'][0][0]
        aspect = sentence[aspect_index]
        return aspect
    
    """ getting one label only """
    def get_label(self, index = 0):
        item = self.output[index]
        label = item['labels'][0]
        return label

    """ getting one sentence only """
    def get_sentence(self, index = 0):
        item = self.output[index]
        sentence = item["sentence"]
        return sentence

    def helper_update_aspect_result(self, aspect_result, label):
        if (label == 1):
            aspect_result['positive'] = aspect_result['positive'] + 1
        elif (label == 0):
            aspect_result['neutral'] = aspect_result['neutral'] + 1
        else:
            aspect_result['negative'] = aspect_result['negative'] + 1
        return aspect_result       

    """getting all aspects and labels"""
    def get_all_aspects_and_labels(self):
        results = {}
        for i in range(len(self.output)):
            aspect = self.get_aspect(i)
            label = self.get_label(i)
            if aspect in results.keys():
                aspect_result = results[aspect]
                aspect_result['count'] = aspect_result['count'] + 1
                aspect_result = self.helper_update_aspect_result(aspect_result, label)               
            else:
                aspect_result = {'count': 1, 'positive': 0,'netural': 0, 'negative':0}
                aspect_result = self.helper_update_aspect_result(aspect_result, label)
                
            results[aspect] = aspect_result
        return results