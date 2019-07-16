import string

class Recomendation:

    def __init__(self,
                 uppercase=0, lowercase=0, numbers=0,
                 special=0, total=0, repeat=True):
        """
        This class offers a password recomendation.\n
        uppercase: minimum number of uppercase letters\n
        lowecase: minimum number of lowercase letters\n
        numbers: minimum number of numbers\n
        special: minimum number of special characters\n
        total: maximum length
        """
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.special = special
        self.total = total
        self.repeat = repeat
    
    def test_password(self, password: str) -> str:
        """
        Tests if the password respect the configuration
        and return a level for the password.\n
        Levels: Strong, Medium, Weak.
        """
        count_lower = 0
        count_upper = 0
        count_number = 0
        count_special = 0
        level = 0
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
        
        if len(password) > 9 and count_special and count_number and count_upper:
            return "Strong"
        if len(password) > 9 and (count_special or count_number or count_upper):
            return "Medium"
        else:
            return "Weak"
    
    def check_dict_password(self, dict: list, password: str) -> bool:
        """
        Check if the dictionary contains the password.
        """
        for word in dict:
            if word == password:
                print('Weak Password: Dictionary password ->' + word)
                return False
        return True