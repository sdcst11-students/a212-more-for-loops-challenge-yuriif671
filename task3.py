#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]

allow = False

username = str(input("Gimme ur name: "))
password = str(input("Gimem ur password: "))

for i in range(len(users)):
    if users[i] == username:
        if passwords[i] == password:
            print("U r in!")
            allow = True
            break

if not allow:
    print("Nuh-uh")