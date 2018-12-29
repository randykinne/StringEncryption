# Randy Kinne
# Program 8
# COMS-170-WWW01: Fall 2017
# Due: 12/4/2017
# Program: String Capitalizer
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# menuSelection         String      Menu selection by user input
# strInput              String      Input sentences by user
# stringList         String<List>   Store strings split by sentence
import time
import sys

def main():
    list1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.','1','2','3','4','5','6','7','8','9','0', ' ']
    list2 = ['4','R','5','G','Z','3','2','D','A','E','X','Y','U','I','6','W','7','O','V','8','F','Q','L','0','J','.','H','9','C','B','N','S','P','M','1','T','K', ' ']

    
    
def menu(title, **kwargs):
    print(">> ", title.title())
    print()

    for key, value in kwargs.items():
        print(">> ", value, " ", key.replace("_", " ").title())

    print()

    selection = input(">> Enter your selection: ")

    if selection in kwargs:
        return selection
    else:
        print(">> Invalid input! Option(s): ", kwargs.items())
        time.sleep(1)
        menu(title, kwargs)

def crypt(message, list1, list2):
    cryptedMessage = ""
    for i in range(len(message)):
        for item in range(len(list1)):
            if (message[i].upper() == list1[item]):
                cryptedMessage += list2[item]

    return cryptedMessage
    

def end(msg="Goodbye!"):
    print(">> ", msg)
    time.sleep(1)
    sys.exit()
    
main()
