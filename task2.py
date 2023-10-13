#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = "systemadmin"
expectedPassword = "master"

allow = False

for i in range(3):
    username = str(input("Gimme ur name: "))
    password = str(input("Gimme ur passsword: "))

    if username == expectedUsername and password == expectedPassword:
        print("U r in!")
        allow = True
        break
    else:
        print("Try again! \n")

if not allow:
    print("Nuh-uh")