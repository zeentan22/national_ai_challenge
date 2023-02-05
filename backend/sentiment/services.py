import re
from abc import ABC, abstractmethod
from .model.model import NLPModel

class LanguageModelServiceInterface(ABC):
    '''
    Interface for NLP model service
    '''
    def __init__(self):
        self.model = None
    
    @abstractmethod
    def predict(self, user_input: str) -> dict:
        '''
        Predicts aspect based user emotion from given language input

        user_input: str
            Sentence from user conversation        

        rtype: List[dict[str, int]]
            Mapping of each aspect to emotion (-1, 0, 1)
                dict_example = {
                    "service" : -1,
                    "food": 1,
                    "price: 0,
                }
        '''
        
        raise NotImplementedError()

    @abstractmethod
    def clean_input(self, user_input: str) -> str:
        '''
        Cleans and prepares input into model
        '''
        return user_input


class SenticGCNService(LanguageModelServiceInterface):
    def __init__(self):
        self.model = NLPModel() 
        
    def predict(self, user_input: str) -> dict:
        cleaned_input = self.clean_input(user_input)

        self.model.set_input({"sentence": cleaned_input})
        self.model.run()
        output = [
            {"aspect": self.model.get_aspect(), "emotion": self.model.get_label()}
        ]
        
        return output
    
        '''
        test_output = [
            {'aspect': 'food', 'emotion': 1},
            {'aspect': 'price', 'emotion': 0},
            {'aspect': 'service', 'emotion': -1},
        ]
        return test_output
        '''        

    def clean_input(self, user_input: str) -> str:
        # change this to tokenise your input

        user_input = re.sub('([.,!?()])', r' \1 ', user_input)
        user_input = re.sub('\s{2,}', ' ', user_input)

        cleaned = user_input

        return cleaned