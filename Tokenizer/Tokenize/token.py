import random
from string import ascii_letters
from string import digits

class Token():
    
    def __init__(self,value):
        self.raw_value=value
        self.token_value = self.get_token()

    def get_token(self):
        '''
        Get length of raw value
        if numeric only ; give numeric  token back
        if alph give alpha back
        ss is future
        give back the same length string
        '''

        possible_values = ascii_letters
        if self.raw_value.isnumeric():
            possible_values = digits
        else:
            possible_values = ascii_letters

        token_value = ''.join(random.choice(possible_values) for _ in range(self.get_raw_value_length()))
        return token_value

    def get_raw_value_length(self):
        return len(self.raw_value)

    def get_token_value_length(self):
        return len(self.token_value)
