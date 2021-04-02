import io 

"""
    Student: Nhi Tran
    Module: gladysUserLogin
    Description: This module checks if the username is a valid email address or not and logs the user in.
"""
def login(email_address):
   while "@" not in email_address:
       email_address = input("User login is not an email address. ")
       if "." not in email_address:
           email_address = input("User login is not an email address. ")
       if "com" not in email_address:
           email_address = input("User login is not an email address. ")
       return email_address

login(input("Username: "))
password = input("Password: ")
