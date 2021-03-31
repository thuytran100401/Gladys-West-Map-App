import io
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

   # delete the remaining code *in this function* and replace it with
   # your code. add more code to do what the assignment asks you to do.
   # add 3 more tests of different functions in different modules
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
   userQuit = False
   while (not userQuit):

       print()
       print("--- Gladys West Map App ---")
       print()

       # menu
       print("[c] to set current position")
       print("[d] to set destination position")
       print("[m] to map - which tells the distance")
       print("[t] to run module tests")
       print("[q] to quit")

       print()
       print("-- Welcome to the Gladys West Map App --")
       print("Type t to run tests or q to quit")
       print()

       # get first character of input
       userInput = input("Enter a command: ")
       lowerInput = userInput.lower()
       firstChar = lowerInput[0:1]

       # set current location
       if firstChar == 'c':

           # set destination position
           if firstChar == 'd':

               # map - tells the distance
               if firstChar == 'm':

                   # quit
                   if firstChar == 'q':
                       userQuit = True

       else:
           print("ERROR: " + firstChar + " is not a valid command")

   print("\n")
   print("Thank you for using the Gladys West Map App!")
   print("\n")


@app.route('/login', methods=['POST'])
def do_admin_login():
  login = request.form

  userName = login['username']
  password = login['password']

  cur = mariadb_connect.cursor(buffered=True)
  data = cur.execute('SELECT * FROM Login WHERE username=%s', (userName))
  data = cur.fetchone()[2]

  if sha256_crypt.verify(password, data):
    account = True

  if account:
    session['logged_in'] = True
  else:
    flash('wrong password!')
  return home()

