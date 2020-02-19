from math import pi;
import os;

print("########## Python Modules ##########")

print("The value of pi is .. ",pi);
with open("log.txt",'a', encoding = 'utf-8') as f:
    #f = open("log.txt",'a')
    f.write(input("what is the day to day .."))
    f.close;
print(os.listdir());

import sys

randomList = ['a', 0, 2, 0.5, '12.09.3']


for entry in randomList:
    try:
        print("The entry is ", entry)
        r = 1/int(entry)
        pass
    except ValueError:
        print("Exception", ValueError, " Occured.")
        print("I'm in the VauleError block")
    except ZeroDivisionError:
        print("Exception", ZeroDivisionError, " Occured.")
        print("I'm in the ZeroDivisionError block")
    except:
        print("Exception:",sys.exc_info()[0], "occured.")
        print("Next entry ..")
        print()
print("The reciprocal of ", entry, "is", r)
    

