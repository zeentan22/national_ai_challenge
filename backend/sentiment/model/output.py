from model import NLPModel



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

model = NLPModel({"sentence": "I dislike the school environment ."})
model.run()
# print(repr(model))

print({"aspect": model.get_aspect(), "label": model.get_label()})

#print(model.get_all_aspects_and_labels())

{
'school': {'count': 2, 'positive': 2, 'netural': 0, 'negative': 0}, 
'students': {'count': 2, 'positive': 2, 'netural': 0, 'negative': 0}, 
'meeting': {'count': 1, 'positive': 1, 'netural': 0, 'negative': 0}
}

