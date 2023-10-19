t=3

psd="DEV@2023"

Password=input("ecrire le mot de pass : ")

q="mrRobot"

while Password!=psd :

    t -=1

    print(f"mot pass incorrecte ")

    Password=input(" ecrire le mot de pass : ")
    

    if t==0 and Password!=psd:

        o=input("donner le nom de film : ")

        if o==q:
            tries=3
        else :
            print("by")
            break

    elif t==0 and Password==psd:

        print("bonjour .")

else :
    if t!=0:
        print("bonjour .")
