import os
from persistence import Persistence
from shadow import Shadow
from recomendation import Recomendation
from users import User, Users
from texttable import Texttable

"""
Main interface of the program.
"""

if __name__ == "__main__":

    recomendation = Recomendation()
    shadow = Shadow("./etc/shadow", recomendation)
    users = Users("./etc/passwd")
    db = Persistence()

    print('''

                                    )                                                                
                          (      ( /(               (                                 )              
          )       (  (    )\ )   )\())  (  (  (     )\ )     (         (  (      ) ( /((             
 `  )  ( /( (  (  )\))(  (()/(  ((_)\  ))\ )\))(   (()/(    ))\ (     ))\ )(  ( /( )\())\  (   (     
 /(/(  )(_)))\ )\((_)()\  ((_))  _((_)/((_((_)()\   /(_))_ /((_))\ ) /((_(()\ )(_)(_))((_) )\  )\ )  
((_)_\((_)_((_((__(()((_) _| |  | \| (_)) _(()((_) (_)) __(_)) _(_/((_))  ((_((_)_| |_ (_)((_)_(_/(  
| '_ \/ _` (_-(_-\ V  V / _` |  | .` / -_)\ V  V /   | (_ / -_| ' \)/ -_)| '_/ _` |  _|| / _ | ' \)) 
| .__/\__,_/__/__/\_/\_/\__,_|  |_|\_\___| \_/\_/     \___\___|_||_|\___||_| \__,_|\__||_\___|_||_|  
|_|                                                                                                  
                                                            
    ''')
    print("Welcome to passwd New Generation. Type 'help' to see the commands.\n")

    while True:
        cmd = input("~ ").split(" ")
        if cmd[0] == "config":
            if cmd[1] == "uppercase":
                recomendation.uppercase = int(cmd[2])
                lastconf = db.get_conf()
                db.add_conf(cmd[2], lastconf[2], lastconf[3], lastconf[4], lastconf[5], lastconf[6])
                print("Minimun uppercase characters changed to " + cmd[2])
            elif cmd[1] == "lowercase":
                recomendation.lowercase = int(cmd[2])
                lastconf = db.get_conf()
                db.add_conf(lastconf[1], cmd[2], lastconf[3], lastconf[4], lastconf[5], lastconf[6])
                print("Minimun lowercase characters changed to " + cmd[2])
            elif cmd[1] == "number":
                recomendation.numbers = int(cmd[2])
                lastconf = db.get_conf()
                db.add_conf(lastconf[1], lastconf[2], cmd[2], lastconf[4], lastconf[5], lastconf[6])
                print("Minimun number characters changed to " + cmd[2])
            elif cmd[1] == "special":
                recomendation.special = int(cmd[2])
                lastconf = db.get_conf()
                db.add_conf(lastconf[1], lastconf[2], lastconf[3], cmd[2], lastconf[5], lastconf[6])
                print("Minimun special characters changed to " + cmd[2])
            elif cmd[1] == "total":
                recomendation.total = int(cmd[2])
                lastconf = db.get_conf()
                db.add_conf(lastconf[1], lastconf[2], lastconf[3], lastconf[4], cmd[2], lastconf[6])
                print("Total characters changed to " + cmd[2])
            elif cmd[1] == "repeat":
                if cmd[2] == "y":
                    recomendation.repeat = True
                    print("Allowed to repeat password")
                elif cmd[2] == "n":
                    recomendation.repeat = False
                    print("Not allowed to repeat password")
                else:
                    print("Error: Unknown command.")
                    continue
            else:
                print("Error: Unknown command.")
        elif cmd[0] == "add":
            user = shadow.add_password(cmd[1], cmd[2]);
            if user:
                db.add_password(user[0], user[1], user[2])
                shadow.save()
                print("Password added succesful")
        elif cmd[0] == "remove":
            if shadow.remove_password(cmd[1]):
                db.add_password(cmd[1], "null", "null")
                shadow.save()
                print("Password removed succesful")
        elif cmd[0] == "lock":
            if shadow.lock(cmd[1]):
                password = db.get_password(cmd[1])
                if len(password) == 0:
                    db.add_password(cmd[1], "null", "null", "Locked")
                else:
                    password = password[-1]
                    db.add_password(cmd[1], password[2], password[3], "Locked")
                print("Password locked succesful")
                shadow.save()
        elif cmd[0] == "unlock":
            if shadow.unlock(cmd[1]):
                print("Password unlocked succesful")
                shadow.save()
        elif cmd[0] == 'show':
            if cmd[1] == 'users':
                table = Texttable()
                table.set_max_width(0)
                table.set_deco(Texttable.HEADER)
                rows = [user.user() for user in users.users]
                rows.insert(0, users.fields())
                table.add_rows(rows)
                print(table.draw())
            elif cmd[1] == 'config':
                table = Texttable()
                table.set_deco(Texttable.HEADER)
                table.set_cols_align(['c','c'])
                conf = db.get_conf()
                table.add_rows([
                    ['Option', 'Value'],
                    ['uppercase', conf[1]],
                    ['lowercase', conf[2]],
                    ['numbers', conf[3]],
                    ['special', conf[4]],
                    ['total', conf[5]],
                    ['period', conf[6]]
                ])
                print(table.draw())
            else:
                print("Unknown command.")
        elif cmd[0] == 'adm':
            if os.geteuid() != 0:
                print("You don't have root privileges.")
            else:
                passwords = db.get_password_groupbyname()
                table = Texttable()
                table.set_max_width(0)
                rows = [[p[1], p[3], p[4], p[5]] for p in passwords]
                rows.insert(0, ['User', 'Password level', 'Status', 'Last change'])
                table.add_rows(rows)
                print(table.draw())
        elif cmd[0] == 'help':
            table = Texttable()
            table.set_deco(Texttable.HEADER)
            if len(cmd) > 1:
                if cmd[1] == 'config':
                    table.add_rows([
                        ['Command', 'Info'],
                        ['config uppercase [value]', 'Set the minimun number of uppercase characters.'],
                        ['config lowercase [value]', 'Set the minimun number of lowercase characters.'],
                        ['config numbers [value]', 'Set the minimun number of numbers.'],
                        ['config special [value]', 'Set the minimun number of special characters.'],
                        ['config repeat [y/n]', "Set 'y' if is allowed to repeat a password"]
                    ])
                else:
                    print("Unknown command.")
            else:
                table.add_rows([
                    ['Command', 'Info'],
                    ['config [option] [value]', 'Configure password recomendation.'],
                    ['add [username] [new password]', 'Add a new password to an user.'],
                    ['remove [username]', 'Remove a password to an user.'],
                    ['lock [username]', 'Lock a password of an user.'],
                    ['unlock [username]', 'Unlock a password of an user'],
                    ['help [command]', 'See more information about a command.'],
                    ['show users', 'Show all the users.'],
                    ['show config', 'Show the configuration of password recomendation.'],
                    ['adm', 'Administrator interface.'],
                    ['exit', 'Exit from passwdNG.']
                ])
            print(table.draw())
        elif cmd[0] == "exit":
            db.close()
            break
        else:
            print("Error: Unknown command.")