# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  
# define our clear function
def cls():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
        print ("")
        print ('CALCULATOR')
        print ("")

  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  
# print out some text
print('hello geeks\n'*200)
  
# sleep for 2 seconds after printing output
sleep(.000000001)
  
# now call function we defined above
cls()
#
# Copied from https://www.geeksforgeeks.org/clear-screen-python/
# Edited clear() to cls()
# Makes more sense to me and easier to type#
#

print ('Loading.\n'*5)
sleep(.2)
cls()
print ('Loading..\n'*5)
sleep(.2)
cls()
print ('Loading...\n'*5)
sleep(.2)
cls()
print ('Loading....\n'*5)
sleep(.2)
cls()
print ('Loading.\n'*5)
sleep(.2)
cls()
print ('Loading..\n'*5)
sleep(.2)
cls()
print ('Loading...\n'*5)
sleep(.2)
cls()
print ('Loading....\n'*5)
sleep(.2)
cls()

print ('Press 1 for Addition')
print ('Press 2 for Subtraction')
print ('Press ENTER to confirm selection')

sel = int (input (""))
#^^^ creates error if input is not a number


if sel == 1 or sel == 2:
    if sel == 1:
        cls()
        print ("ADDITION")
        print ("")

        #x print ("How many digits would you like to add?")
        #x poly = int (input (""))
        #x cls()
        a = int(input('First number ->'))
        b = int(input('Next number  ->'))

        print (a,"+",b,"=",a+b)


    if sel == 2:
        cls()
        print ('SUBTRACTION')

else:
    cls()
    print ('*UNKNOWN ENTRY, TRY AGAIN*')



    
