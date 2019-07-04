from shadow import Shadow
from recomendation import Recomendation

if __name__ == "__main__":

    recomendation = Recomendation()
    shadow = Shadow("etc/shadow", recomendation)

    print("*********************************")
    print("***** Passwd New Generation *****")
    print("*********************************")
    while True:
        cmd = input().split(" ")
        if cmd[0] == "config":
            if cmd[1] == "uppercase":
                recomendation.uppercase = int(cmd[2])
                print("Minimun uppercase characters changed to " + cmd[2])
            if cmd[1] == "lowercase":
                recomendation.lowercase = int(cmd[2])
                print("Minimun lowercase characters changed to " + cmd[2])
            if cmd[1] == "number":
                recomendation.numbers = int(cmd[2])
                print("Minimun number characters changed to " + cmd[2])
            if cmd[1] == "number":
                recomendation.numbers = int(cmd[2])
                print("Minimun number characters changed to " + cmd[2])
            if cmd[1] == "special":
                recomendation.special = int(cmd[2])
                print("Minimun special characters changed to " + cmd[2])
            if cmd[1] == "total":
                recomendation.total = int(cmd[2])
                print("Total characters changed to " + cmd[2])
            if cmd[1] == "repeat":
                if cmd[2] == "y":
                    recomendation.repeat = True
                    print("Allowed to repeat password")
                elif cmd[2] == "n":
                    recomendation.repeat = False
                    print("Not allowed to repeat password")
                else:
                    print("Error: Unknown command.")
                    continue
        elif cmd[0] == "addpassword":
            if shadow.add_password(cmd[1], cmd[2]):
                print("Password added succesful")
                shadow.save()
        elif cmd[0] == "rempassword":
            if shadow.remove_password(cmd[1]):
                print("Password removed succesful")
                shadow.save()
        elif cmd[0] == "lock":
            if shadow.lock(cmd[1]):
                print("Password locked succesful")
                shadow.save()
        elif cmd[0] == "unlock":
            if shadow.unlock(cmd[1]):
                print("Password unlocked succesful")
                shadow.save()
        elif cmd[0] == "exit":
            break
        else:
            print("Error: Unknown command.")