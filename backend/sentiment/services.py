from abc import ABC, abstractmethod

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
        self.model = None 
        
    def predict(self, user_input: str) -> dict:
        cleaned_input = self.clean_input(user_input)

        test_output = [
            {'aspect': 'food', 'emotion': 1},
            {'aspect': 'price', 'emotion': 0},
            {'aspect': 'service', 'emotion': -1},
        ]

        return test_output

    def clean_input(self, user_input: str) -> str:
        # change this to tokenise your input

        cleaned = user_input \
                    .replace("(", "-LRB-") \
                    .replace(")", "-RRB-")
        
        return cleaned