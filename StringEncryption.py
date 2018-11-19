# Randy Kinne
# COMS-170-WWW01: Fall 2017
# Due: 12/18/2017
# Program: String Encryption
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# isWelcome           Boolean       Whether to print welcome screen on call of main()
# selection            String       Menu selection by user input
# list1               String<List>  String list of alphabet 1
# list2               String<List>  String list of alphabet 2
# strInput             String       Input sentences by user
# times                Int          Number of times to encrypt/decrypt (default 1)
# message             String        Store message to print to user
# arg                *args<String>   Used in printBars() to add lines to print
# title               String        Used in menu() to print menu title
# large               Boolean       Used in menu() to determine whether to print large title or compact title
# kwargs       **kwargs<String><Int> Used in menu() to store key, value
# cryptedMessage     String         Used in crypt() to store/create the crypted message after it's been crypted
# stringList         String<List>   Store strings split by sentence

import time
import sys
import random

def main(isWelcome=True):
    # print greeting for user if isWelcome is True
    # isWelcome is default set to True but most times called it's set to false
    if (isWelcome):
        welcome()

    # create and store lists that correlate values
    list1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.','1','2','3','4','5','6','7','8','9','0', ' ', ',', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '~', '/', '?', '|', '"\"']
    list2 = ['4','R','5','G','Z','3','2','D','A','E','X','Y','U','I','6','W','7','O','V','8','F','Q','L','0','J','.','H','9','C','B','N','S','P','M','1','T','K', ' ', ',', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '~', '/', '?', '|', '"\"']
    
    # print menu for user named 'menu', large menu, main menu options
    selection = menu("Menu", True, ENCRYPT="1", DECRYPT="2", HELP="3", EXIT="0")

    # print empty line for user to separate important details
    print()

    # if user selects 1/encryption at main menu
    if (selection == "1"):

        # clear all lines written above
        clear()
        # print title bars as well as description lines
        printBars("Encryption", "Maximum number of times: 10,000", "Minimum number of times: 1", "Enter 1 for default encryption", "Enter 'R' for random")
        # print empty line for user
        print()

        # ask user to input the sentence(s) they want encrypted
        strInput = input(">> Enter the sentence(s) to encrypt: ")

        # ask user to input the amount of times they want it encrypted
        # for default encryption, enter 1
        # custom number of times can be input to hypothetically increase the difficulty to solve
        # if a user looked at the code they would know the direct value, but unless they knew the specific number they wouldn't be able to decrypt it, theoretically
        # feature added beyond program basic instructions for final project to increase program's useability
        times = input(">> Enter the number of times to encrypt: ")

        # if user selects, random, set time to random int between 1 and 10,000
        # after testing i've found that selecting numbers much larger than 10,000 creates considerable delay in time to encrypt
        # theoretically, it shouldn't take many more encryption times beyond 10,000 for most basic uses
        # also, try except in case they don't enter 'R' or a valid integer
        if (str(times).upper() == "R"):
            times = random.randint(1, 10000)
        else:
            try:
                times = int(times)
            except ValueError:
                print(">> ValueError: Input invalid, defaulting to value of 1")
                times = 1

        # enforce time between 1 and 10,000
        if (times <= 0 or times > 10000):
            print(">> Number of times cannot be less than 1 or greater than 10,000. Defaulting to 1.")
            times = 1
        # crypt the message at least once
        message = crypt(strInput, list1, list2)
        # for each time more than one, iterate through and crypt again
        if (times > 1):
            for i in range(times - 1):
                message = crypt(message, list1, list2)

        # print output for user, formatted for consistency
        print()
        print(">> Output encrypted", times, "time(s):", message)
        print()

        # allow user to copy/see message before printing more lines
        # don't clear here so that the user can still see the message they need
        time.sleep(2.5)
        # create menu to continue/return to menu or quit program
        selection = menu("Continue?", False, RETURN_TO_MENU="1", HELP="2", EXIT="0")

        # action based on menu selection
        if (selection == "1"):
            main(False)
        elif (selection == "0"):
            quitProgram("Bye")
        elif (selection == "2"):
            help()
        else:
            print(">> Invalid Input")
            time.sleep(1)
            main(False)

    # if user selects 2/decryption at main menu
    elif (selection == "2"):
        # print bars/descriptive strings for user, formatted for consistency
        printBars("Decryption", "Maximum number of times: 10,000", "Minimum number of times: 1", "Enter 1 for default decryption", "Enter 'R' for random")
        print()

        # get user input for the sentence they want to decrypt
        strInput = input(">> Enter the sentence(s) to decrypt: ")

        # get the amount of times they want to decrypt
        # for more information, look to the times comment in Encryption above
        times = input(">> Enter the number of times to decrypt (default is 1, enter 'R' for random): ")

        # if user selects random, select random int between 1 and 10,000
        # try except for invalid input, default values set to 1 and notify user if they are forced
        if (times == "R"):
            times = random.randint(1, 10000)
        else:
            try:
                times = int(times)
            except ValueError:
                print(">> ValueError: Input invalid, defaulting to value of 1")
                times = 1

        # force times to be between 1 and 10,000
        if (times <= 0 or times > 10000):
            print(">> Number of times cannot be less than 1 or greater than 10,000. Defaulting to 1.")
            times = 1
            
        # output for user
        print(">> DECRYPTED MESSAGE")
        print()

        # decrypt at least once
        message = crypt(strInput, list2, list1)

        # decrypt for each iteration of added amount of times to decrypt
        if (times > 1):
            for i in range(times - 1):
                message = crypt(message, list2, list1)
        # print output for user
        print(">> Output decrypted", times, "time(s):", message)
        time.sleep(2.5)
        # print menu for user to continue/return to menu or exit
        selection = menu("Continue?", False, RETURN_TO_MENU="1", HELP="2", EXIT="0")
            
        if (selection == "1"):
            main(False)
        elif (selection == "0"):
            quitProgram("Bye")

    # if user selects 0/quit from main menu           
    elif (selection == "0"):
        quitProgram()

    # if user selects 3/help from main menu
    elif (selection == "3"):
        help()


def welcome():
    # print greeting for user, welcome screen
    clear()
    printBar()
    print()
    print("      String Encryption       ")
    print()
    print("    Program by Randy Kinne    ")
    print()
    printBar()
    time.sleep(2)
    clear()

# help for users
def help():
    # print help screen
    clear()
    printBars("Help Menu - String Encryption")
    print(">> Encryption - Enter a string to encrypt. Valid characters are A-Z.0-9",
          "",
          ">> Times to encrypt can be used to further encrypt the encrypted string.",
          ">> Theoretically it enhances the encryption since you need the to know the num-",
          ">>  ber of times to decrypt the message accurately.",
          "",
          ">> The default amount for standard encryption used in the program requirements is 1",
          sep="\n")

    print()
    printBar()
    print()

    print(">> Decryption - Enter an encrypted string to decrypt. Valid characters are A-Z.0-9",
          "",
          ">> Times to decrypt are used to accurately decrypt the encrypted string",
          ">> Must know the number of times it was encrypted to accurately decrypt the message.",
          "",
          ">> The default amount for standard encryption used in the program requirements is 1",
          sep="\n")

    print()
    printBar()
    print()
    
    input(">> Press 'enter' to return to main menu: ")
    main(False)

# clear screen for user to keep output from piling up
# default amount is 100 but custom amount can be used
def clear(amt=100):
    print("\n" * amt)

# bar, used in menus to separate headings/information
def printBar():
    print("=======================================================")

# primary headings used in most menus
def printBars(text, *args):
    printBar()
    print()
    print(">> ", text.title(), sep="")
    print()
    printBar()
    print()
    for arg in args:
        print(">>", arg)

# menu function, can be almost completely customized for different looks
# title - title of menu
# large - large or small menu, large has heading in printBars small is just a simple question with options for an answer
# kwargs - custom key, value dictionary set for adding possible options in menus
def menu(title, large, **kwargs):
    # if menu is to be large
    if (large):
        # clear the screen
        clear()
        # create title with bars, more large 
        printBars(title)
        print()

        print(">> OPTIONS:")
    # if menu is not to be large
    else:
        # print one bar
        printBar()
        print()
        # print small title
        print(">> ", title.upper(), ":", sep="")

    # iterate through all entries in kwargs to print all options in a standardized format
    for key, value in kwargs.items():
        print(">> ", value, ": ", key.replace("_"," ").title(), sep="")

    # get user input from their menu choice
    selection = input(">> Enter your selection: ")

    # if their selection is a number that corresponds to a value in kwargs
    if selection in kwargs.values():
        return selection;
    # if their selection is a string that corresponds to a key in kwargs, return the corresponding value in kwargs so that the code in main() can use it
    elif selection.upper() in kwargs.keys():
        return kwargs[selection.upper()]
    # if their selection is not in kwargs or otherwise invalid, repeat menu
    else:
        print()
        print(">> Invalid input! Option(s): ", str(kwargs).replace("{", "").replace("}", ""))
        print()
        time.sleep(1.5)
        # keep printing new menus until a valid selection is input by user
        return menu(title, False, **kwargs)

# actual function for encryption/decryption
# actually pretty complex
# switches between encryption and decryption based on which list is entered first and second
def crypt(message, list1, list2):
    # create cryptedMessage variable
    cryptedMessage = ""
    # for each character in message, iterate through each item in list1
    # if the character matches the item, add the corresponding index of item from list2 to cryptedMessage
    for i in range(len(message)):
        # iterate through each item in list1
        for item in range(len(list1)):
            # if the character matches the item, add the index of item from list2 to cryptedMessage
            if (message[i].upper() == list1[item]):
                cryptedMessage += list2[item]

    # return the cryptedMessage once the iteration of characters is complete
    return cryptedMessage

# function for safely and verbosely shutting down the program
def quitProgram(msg="Goodbye!"):
    print(">> ", msg)
    time.sleep(1)
    sys.exit()

# call main with isWelcome defaulted to True to display welcome screen
main()

# End of program

# Compiled and ran program below is condensed
# Extra whitespaces between messages used to clear output in the actual program itself
# was removed for faster read-ability 

##Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
##[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
##Type "copyright", "credits" or "license()" for more information.
##>>> 
## RESTART: /Users/randykinne/Desktop/School/2017/Programming/ProgramFinalProject.py 
##
##=======================================================
##
##      String Encryption       
##
##    Program by Randy Kinne    
##
##=======================================================
##
##=======================================================
##
##>> Menu
##
##=======================================================
##
##
##>> OPTIONS:
##>> 1: Encrypt
##>> 2: Decrypt
##>> 3: Help
##>> 0: Exit
##>> Enter your selection: 1
##
##
##=======================================================
##
##>> Encryption
##
##=======================================================
##
##>> Maximum number of times: 10,000
##>> Minimum number of times: 1
##>> Enter 1 for default encryption
##>> Enter 'R' for random
##
##>> Enter the sentence(s) to encrypt: I LOVE COMPUTERS. 
##>> Enter the number of times to encrypt: 1
##
##>> Output encrypted 1 times: A Y6QZ 56UWF8ZOVH 
##
##=======================================================
##
##>> CONTINUE?:
##>> 1: Return To Menu
##>> 2: Help
##>> 0: Exit
##>> Enter your selection: 1
##
##=======================================================
##
##>> Menu
##
##=======================================================
##
##
##>> OPTIONS:
##>> 1: Encrypt
##>> 2: Decrypt
##>> 3: Help
##>> 0: Exit
##>> Enter your selection: 2
##
##=======================================================
##
##>> Decryption
##
##=======================================================
##
##>> Maximum number of times: 10,000
##>> Minimum number of times: 1
##>> Enter 1 for default decryption
##>> Enter 'R' for random
##
##>> Enter the sentence(s) to decrypt: A Y6QZ 56UWF8ZOVH 
##>> Enter the number of times to decrypt (default is 1, enter 'R' for random): 1
##>> DECRYPTED MESSAGE
##
##>> Output decrypted 1 times: I LOVE COMPUTERS. 
##=======================================================
##
##>> CONTINUE?:
##>> 1: Return To Menu
##>> 2: Help
##>> 0: Exit
##>> Enter your selection: 1
##
##
##=======================================================
##
##>> Menu
##
##=======================================================
##
##
##>> OPTIONS:
##>> 1: Encrypt
##>> 2: Decrypt
##>> 3: Help
##>> 0: Exit
##>> Enter your selection: 0
##
##>>  Goodbye!
##>>> 
##
