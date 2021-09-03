# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  
# print out some text
print('hello geeks\n'*20)
  
# sleep for 2 seconds after printing output
sleep(1)
  
# now call function we defined above
clear()
#
#
#
# Copied from https://www.geeksforgeeks.org/clear-screen-python/
#
#
#


print ('')
print ('CALCULATOR')
print ('')
print ('Press 1 for Addition')
print ('Press 2 for Subtraction')
print ('Press ENTER to confirm selection')

sel = int (input (""))
#^^^ creates error if input is not a number


if sel == 1 or sel == 2:
    if sel == 1:
        clear()
        print ("")
        print ("ADDITION")
    if sel == 2:
        clear()
        print ("")
        print ('SUBTRACTION')

else:
    clear()
    print("")
    print ('*UNKNOWN ENTRY, TRY AGAIN*')
    
