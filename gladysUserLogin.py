import io 

"""
    Student: Ngan Hoang
    Module: gladysUserLogin
    Description: This module logs the user in and tell if the email is valid or not.
"""
def login(email_address):
   while "@" not in email_address:
       email_address = input("Invalid email address. ")
       if "." not in email_address:
           email_address = input("Invalid email address. ")
       if "com" not in email_address:
           email_address = input("Invalid email address. ")
       return email_address

login(input("Username: "))
password = input("Password: ")
