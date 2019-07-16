import sys
import crypt
from recomendation import Recomendation

class Options:
    USER = 0
    PASSWORD = 1
    LAST_ALTERATION = 2
    DAYS_TO_ALTERATE = 3
    DAYS_TO_EXPIRATE = 4
    DAYS_TO_DISABLE = 5
    DAYS_DISABLED = 6
    RESERVED = 7
    
class Shadow:
    
    '''
    This class manipulates the shadow file
    '''

    def __init__(self, path: str, recomendation: Recomendation):
        self.path = path
        self.users = []
        self.recomendation = recomendation
        with open(path, 'r') as shadow:
            for line in shadow.readlines():
                self.users.append(line.split(':'))
    
    def get_user(self, username):
        for user in self.users:
            if user[Options.USER] == username:
                return user    
    
    def add_password(self, username: str, password: str):
        user = self.get_user(username)
        if not user:
            print("User does not exists")
            return
        
        dict = open('dict.txt', 'r')
        pass_level = self.recomendation.test_password(password)

        if (pass_level and self.recomendation.check_dict_password(dict, password)):
            pass_crypt = crypt.crypt(password, crypt._Method('SHA512', '6', 8, 106))
            user[Options.PASSWORD] = pass_crypt
            return (username, pass_crypt, pass_level)
    
    def remove_password(self, username: str):
        user = self.get_user(username)
        if user:
            user[Options.PASSWORD] = '*'
            return True
        print('User doesnt exists')
    
    def lock(self, username: str):
        user = self.get_user(username)
        if user:
            if user[Options.PASSWORD][0] == '!':
                print('This user is already locked.')
                return False
            else:
                user[Options.PASSWORD] = '!' + user[Options.PASSWORD]
            return user
        print('User doesnt exists')

    def unlock(self, username: str):
        user = self.get_user(username)
        if user:
            if user[Options.PASSWORD][0] == '!':
                user[Options.PASSWORD] = user[Options.PASSWORD][1:]
            else:
                print('This user is not locked.')
                return False
            return user
        print('User doesnt exists')

    def save(self):
        shadow = []
        for user in self.users:
            shadow.append(':'.join(user))
        shadow_file = open(self.path, 'w')
        shadow_file.writelines(shadow)
        shadow_file.close() 