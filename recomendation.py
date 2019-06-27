import string

class Recomendation:

    def __init__(self,
                 uppercase: int, lowercase: int, numbers: int,
                 special: int, total: int, repetition=True):
        """
        uppercase: minimum number of uppercase letters\n
        lowecase: minimum number of lowercase letters\n
        numbers: minimum number of numbers\n
        special: minimum number of special characters\n
        total: maximum size
        """
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.special = special
        self.total = total
        self.repetition = repetition
    
    def test_password(self, password: str) -> bool:
        count_lower = 0
        count_upper = 0
        count_number = 0
        count_special = 0
        for c in password:
            if c in string.ascii_uppercase:
                count_upper += 1
            if c in string.ascii_lowercase:
                count_lower += 1
            if c in string.digits:
                count_number += 1
            if c in string.punctuation:
                count_special += 1
        if count_upper < self.uppercase:
            print('Uppercase characters lower than recomended. Minimum {}, you have {}.'
                  .format(self.uppercase, count_upper))
            return False
        if count_lower < self.lowercase:
            print('Lowercase characters lower than recomended. Minimum {}, you have {}.'
                  .format(self.lowercase, count_lower))
            return False
        if count_number < self.numbers:
            print('Number characters lower than recomended. Minimum {}, you have {}.'
                  .format(self.numbers, count_number))
            return False
        if count_special < self.special:
            print('Special characters lower than recomended. Minimum {}, you have {}.'
                  .format(self.special, count_special))
            return False
        return True