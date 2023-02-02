from sgnlp.models.sentic_gcn import(
    SenticGCNBertConfig,
    SenticGCNBertModel,
    SenticGCNBertEmbeddingConfig,
    SenticGCNBertEmbeddingModel,
    SenticGCNBertTokenizer,
    SenticGCNBertPreprocessor,
    SenticGCNBertPostprocessor
)
tokenizer = SenticGCNBertTokenizer.from_pretrained("bert-base-uncased")

config = SenticGCNBertConfig.from_pretrained(
    "./senticgcnbert/config.json")
model = SenticGCNBertModel.from_pretrained(
    "./senticgcnbert/pytorch_model.bin",
    config=config
)
embed_config = SenticGCNBertEmbeddingConfig.from_pretrained("bert-base-uncased")

embed_model = SenticGCNBertEmbeddingModel.from_pretrained("bert-base-uncased",
    config=embed_config
)
preprocessor = SenticGCNBertPreprocessor(
    tokenizer=tokenizer, embedding_model=embed_model,
    senticnet="./senticNet/senticnet.pickle",
    device="cpu")

postprocessor = SenticGCNBertPostprocessor()

class nlp_model:
    def __init__(self, inputs):
        self.inputs = inputs
        self.output = None

    def __repr__(self):
        print("hello")
        print(self.output)
        rep = f"Model output is {self.output}"
        return rep

    def run(self):
        processed_inputs, processed_indices = preprocessor(self.inputs)
        raw_outputs = model(processed_indices)
        post_outputs = postprocessor(processed_inputs=processed_inputs, model_outputs=raw_outputs)
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
                



    

