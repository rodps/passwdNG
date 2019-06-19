import sys
import crypt, string, random

class Shadow():

    def __init__(self, lines: list):
        self.users = []
        for line in lines:
            info = line.split(':')
            self.users.append({
                'user': info[0],
                'password': info[1],
                'last_alteration': info[2],
                'days_to_alterate': info[3],
                'days_to_expirate': info[4],
                'days_to_disable': info[5],
                'days_of_disable': info[6],
                'reserved': info[7]
            })
    
    def add_password(self, username: str, password: str):
        pass_crypt = crypt.crypt(password, crypt.METHOD_SHA512)
        user = get_user(username)
        if user:
            user['password'] = pass_crypt
            return user
        print('User doesnt exists')
    
    def remove_password(self, username: str):
        user = get_user(username)
        if user:
            user['password'] = '*'
            return user
        print('User doesnt exists')
    
    def lock(self, username: str):
        user = get_user(username)
        if user:
            user['password'] = '!' + user['password']
            return user
        print('User doesnt exists')

    def unlock(self, username: str):
        user = get_user(username)
        if user:
            user['password'] = '!' + user['password']
            return user
        print('User doesnt exists')

    def get_shadow(self):
        shadow = []
        for user in self.users:
            shadow.append(':'.join(list(user.values())))
        return shadow

    def get_user(self, username):
        for user in self.users:
            if user['user'] == username:
                return user        

# def make_salt8():
#     return '$6$'+''.join(random.choice(string.ascii_letters + string.digits + '.' + '/') for _ in range(8))

shadow = open('etc/shadow', 'r')
s = Shadow(shadow.readlines())