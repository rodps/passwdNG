import sys
import crypt, string, random

class Options():
    USER = 0
    PASSWORD = 1
    LAST_ALTERATION = 2
    DAYS_TO_ALTERATE = 3
    DAYS_TO_EXPIRATE = 4
    DAYS_TO_DISABLE = 5
    DAYS_OF_DISABLE = 6
    RESERVED = 7
    
class Shadow():

    def __init__(self, lines: list):
        self.users = []
        for line in lines:
            info = line.split(':')
            self.users.append(info)
    
    def get_user(self, username):
        for user in self.users:
            if user[Options.USER] == username:
                return user    
    
    def add_password(self, username: str, password: str):
        pass_crypt = crypt.crypt(password, crypt._Method('SHA512', '6', 8, 106))
        user = self.get_user(username)
        if user:
            user[Options.PASSWORD] = pass_crypt
            return user
        print('User doesnt exists')
    
    def remove_password(self, username: str):
        user = self.get_user(username)
        if user:
            user[Options.PASSWORD] = '*'
            return user
        print('User doesnt exists')
    
    def lock(self, username: str):
        user = self.get_user(username)
        if user:
            if user[Options.PASSWORD][0] == '!':
                print('This user is already locked.')
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
            return user
        print('User doesnt exists')

    def get_shadow(self):
        shadow = []
        for user in self.users:
            shadow.append(':'.join(user))
            print(shadow)
        return shadow    

shadow = open('etc/shadow', 'r')
s = Shadow(shadow.readlines())
shadow.close()

s.add_password('mysql', '123mud')

shadow = open('etc/shadow', 'w')
shadow.writelines(s.get_shadow())
shadow.close()