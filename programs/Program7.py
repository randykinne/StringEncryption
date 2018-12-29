# Randy Kinne
# Program 8
# COMS-170-WWW01: Fall 2017
# Due: 12/4/2017
# Program: Grade Average Calculator
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# gradeList             List<Int>       Storing inputted range
# grade                 String      Input by user
#

def main():
    print("################################")
    print("#                              #")
    print("#      String Capitalizer      #")
    print("#                              #")
    print("#    Program by Randy Kinne    #")
    print("#                              #")
    print("################################")

    print(">> MENU")
    print()
    print(">> 1: String Capitalizer")
    print(">> 0: Exit Program")
    print()
    menuSelection = input(">> Enter your selection: ")
    if (menuSelection == "1"):
        strInput = input(">> Enter your sentences: ")
        string = strInput.split(". ")
        for i in string:
            print(i.strip().capitalize().replace(". ", "") + ". ", end="")
    elif (menuSelection == "0"):
        print(">> Goodbye!")

    else:
        print(">> Invalid input! Option(s): 1, 0")
        main()
main()
