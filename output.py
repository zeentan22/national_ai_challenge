from model import nlp_model



inputs = [
    {  # Single word aspect
        "aspects": ["school"],
        "sentence": "The school is a conducive environment for me  ."
    },
    {
        "aspects": ["students"],
        "sentence": "My students are very naughty .",
        
    },
    {
        "aspects": ["students"],
        "sentence": "My students are very good .",
        
    },
    {
        "aspects": ["assignments"],
        "sentence": "My students are very good .",
        
    },
    {
        "aspects": ["meeting"],
        "sentence": "Parent teacher meeting is conducted annually .",
        
    },
    {
        "aspects" : ["school"],
        "sentence": "I dislike the school environment ."
    }
]

model = nlp_model(inputs)
model.run()
print(repr(model))
print(model.get_all_aspects_and_labels())


