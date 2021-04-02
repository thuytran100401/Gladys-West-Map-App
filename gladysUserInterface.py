import io
import math

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
    Student: Khuong Le
    Module: gladysUserInterface
    Description: This module does …
"""
 
 
def runTests():
   """
       tests some module functions
   """

   print("running a few tests")

   average = compute.gpsAverage(4, 5)
   print("average = ", average)

   
   print("hello!")


def start():
   """
       logs the user in, and runs the app
   """

   userName = userLogin.login()
   runApp(userName)



def runApp(userName):
  """
    runs the app
  """
  current = [-1,-1]
  destination = [-1,-1]

  userQuit = False
  while (not userQuit):

    print("---------------------------")
    print("    Gladys West Map App    ")
    print("---------------------------")

    print("\nUser: " + userName)
    print("\ncurrent position   : x =", current[0], " , y = ", current[1])
    print("destination position : x = ", destination[0], " , y = ",destination[1])
    print("distance             : ", round(compute.distance(current, destination),2))

    # menu    
    print("[c] to set current position")
    print("[d] to set destination position")
    print("[m] to map - which tells the distance")
    print("[t] to run module tests")
    print("[q] to quit")

    print()

    # get first character of input
    userInput = input("Enter a command: ")
    lowerInput = userInput.lower()
    firstChar = lowerInput[0:1]

    # set current location
    if firstChar == 'c':
      current[0] = int(input("Enter a x position: "))
      current[1] = int(input("Enter a y position: "))
      
    
    elif firstChar == 'd':
      destination[0] = int(input("Enter a x position: "))
      destination[1] = int(input("Enter a y position: "))
    
    elif firstChar == 'm':
      print(compute.distance(current, destination))

    elif firstChar == 't':
      runtests()
    
    elif firstChar == 'q':
      userQuit = True
      
    else:
      print("ERROR: " + firstChar + " is not a valid command")

  print("\n")
  print("Thank you for using the Gladys West Map App!")
  print("\n")



