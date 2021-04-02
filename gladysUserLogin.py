import io 

"""
    Student: Nhi Tran
    Module: gladysUserLogin
    Description: This module checks if the username is a valid email address or not and logs the user in.
"""
def login():
    emailAddress = ""
    password = ""
    while emailAddress == "":
        emailAddress = input("Enter login: ")
        password = input("Enter password: ")
        if '@' not in emailAddress:
           print("User login is not an email address. ")
           emailAddress = ""
        elif ".com" not in emailAddress:
           print("User login is not an email address. ")
           emailAddress = ""
        else: 
            break

    return emailAddress
