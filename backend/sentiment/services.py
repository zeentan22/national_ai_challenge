# service layer for calling SenticGCN model

class SenticGCNService:
    def __init__(self):
        self.model = None 
        
    def predict(self, input: str) -> dict:
        '''
        Predicts aspect based user emotion from given language input

        input: str
            Sentence from user conversation        

        rtype: List[dict[str, int]]
            Mapping of each aspect to emotion (-1, 0, 1)
                dict_example = {
                    "service" : -1,
                    "food": 1,
                    "price: 0,
                }
        '''
        return [
            {'aspect': 'item1', 'emotion': 1},
            {'aspect': 'item2', 'emotion': -1}
        ]
