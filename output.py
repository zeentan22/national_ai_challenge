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

inputs = [
    {  # Single word aspect
        "aspects": ["scripts"],
        "sentence": "Today is a bad day as I have many scripts to mark .",
    }
]

processed_inputs, processed_indices = preprocessor(inputs)
raw_outputs = model(processed_indices)

post_outputs = postprocessor(processed_inputs=processed_inputs, model_outputs=raw_outputs)

print(post_outputs)



