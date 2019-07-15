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
    
    def __init__(self, passwd_path: str):
        self.users = []
        with open(passwd_path) as passwd_file:
            for line in passwd_file.readlines():
                data = line.split(':')
                self.users.append(User(data[0], data[2], data[3], data[4], data[5], data[6]))
    
    def users(self) -> list:
        return self.users
    
    def fields(self) -> list:
        return ['name', 'uid', 'gid', 'info', 'home', 'shell']
            