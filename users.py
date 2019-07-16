import threading
import time

class User:
    
    def __init__(self, name, uid, gid, info, home, shell):
        self.name = name
        self.uid = uid
        self.gid = gid
        self.info = info
        self.home = home
        self.shell = shell
    
    def user(self):
        return [self.name, self.uid, self.gid, self.info, self.home, self.shell]

class Users:
    
    '''
    This class represents a list of users in passwd file.
    '''

    def __init__(self, passwd_path: str):
        self.passwd_path = passwd_path
        self.users = self.read_passwd()
        t = threading.Thread(target=self.check_uid)
        t.start()
    
    def users(self) -> list:
        return self.users
    
    def read_passwd(self):
        users = []
        with open(self.passwd_path) as passwd_file:
            for line in passwd_file.readlines():
                data = line.split(':')
                users.append(User(data[0], data[2], data[3], data[4], data[5], data[6]))
        return users

    def check_uid(self):
        while True:
            current_users = self.read_passwd()
            for c in current_users:
                for u in self.users:
                    if c.name == u.name and c.uid != u.uid:
                        print('{} UID was modified from {} to {}'.format(c.name, u.uid, c.uid))
            self.users = current_users
            time.sleep(10)

    def fields(self) -> list:
        return ['name', 'uid', 'gid', 'info', 'home', 'shell']
    