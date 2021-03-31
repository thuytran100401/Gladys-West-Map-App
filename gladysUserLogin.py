import io 

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
