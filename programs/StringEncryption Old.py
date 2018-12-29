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
import os

def main():
    # print greeting for user
    welcome()

    list1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.','1','2','3','4','5','6','7','8','9','0', ' ']
    list2 = ['4','R','5','G','Z','3','2','D','A','E','X','Y','U','I','6','W','7','O','V','8','F','Q','L','0','J','.','H','9','C','B','N','S','P','M','1','T','K', ' ']

    validSelection = False
    # print menu for user
    while (validSelection == False):
        selection = menuSelect("Menu", ENCRYPT="1", DECRYPT="2", EXIT="0")

         # if user selects option "1"
        if (selection == "1"):
            validSelection = True
           # ask user to input the sentence(s) they want encrypted
            strInput = input(">> Enter the sentence(s) to encrypt: ")

            # output for user
            print()
            print(">> ", end="")
            print(crypt(strInput, list1, list2))
            print()
            time.sleep(1)
            selection = menuSelect("Continue?", RETURN_TO_MENU="1", EXIT="0")
            if (selection == "1"):
                main()
            elif (selection == "0"):
                quitProgram("Bye")

        elif (selection == "2"):
            validSelection = True
            printBar()
            strInput = input(">> Enter the sentence(s) to decrypt: ")
    
            # output for user
            print(">> ENCRYPTED MESSAGE")
            print()
            print(">> ", crypt(strInput, list2, list1))
            printBar()
            time.sleep(1)
            selection = menuSelect("Continue?", RETURN_TO_MENU="1", EXIT="0")
            if (selection == "1"):
                main()
            elif (selection == "0"):
                quitProgram("Bye")
            
        elif (selection == "0"):
            validSelection = True
            quitProgram()
    
        else:
            print(">> Invalid input! Option(s): 1=Encrypt, 2=Decrypt, 0=Exit")
            main()

def welcome():
    # print greeting for user
    printBar()
    print()
    print("      String Encryption       ")
    print()
    print("    Program by Randy Kinne    ")
    print()
    printBar()
    time.sleep(1)
    clear()

def printBar():
    print("================================")

def clear():
    print("\n" * 100)

def menuSelect(title, **kwargs):
    print(">> ", title.title());
    print()
              
    for key, value in kwargs.items():
        print(">> ", value, " ", key.replace("_"," ").title())
              
    print()
    selection = input(">> Enter your selection: ")

    return selection

def crypt(message, list1, list2):
    cryptedMessage = ""
    for i in range(len(message)):
        for item in range(len(list1)):
            if (message[i].upper() == list1[item]):
                cryptedMessage += list2[item]

    return cryptedMessage

def quitProgram(msg="Goodbye!"):
    print(">> ", msg)
    time.sleep(1)
    sys.exit()
    
main()
# End of program
