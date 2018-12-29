# Randy Kinne
# Program 6
# COMS-170-WWW01: Fall 2017
# Due: 10/02/2017
# Program: Month Converter
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# date                    Integer     Month in number format
# month                  String       Month in string type
#
# ------------------------------------------------------------------
# Function              Return Type     Purpose
# ------------------------------------------------------------------
# printUpdate()              Int             Asks user for a number of the month via input()
# checkDate()           String           Evaluates numerical value of var date and assigns a month based on it, not unlike a switch-case

# import modules
import time
import sys

def printUpdate():
    time.sleep(0.5)
    print(".", end="")
    
# verbose messages for user to see, added timings for user effect
print("Opening file numdata.txt", end="")
for i in range(0, 3):
    printUpdate()

# Open file numdata.txt, if it doesn't exist IOError exception is raised
try:
    f = open("numdata.txt")
except:
    print("\nIOError Exception: File numdata.txt not found!")
    print("\nMake sure the file name is spelled correctly and \nit is in the same location as this program and try again.")
    sys.exit()

# create variables, default values = 0
avgScore = 0
numDataLength = 0

# more verbose messages for user
print("\n\nnumdata.txt found!")

time.sleep(1)
print("\nReading file numData.txt", end="")

# get all values in numdata file, add their values and increment numDataLength to use as denominator in average calculation
for line in f:
    try:
        avgScore = avgScore + int(line.replace("%", ""))
        numDataLength = numDataLength + 1
    except:
        print("\nValueError Exception: File numdata.txt contains characters other than numbers!")
        if (avgScore == 0):
            sys.exit()
        else:
            print("Continuing anyway...") #can continue and still print an average
            print("Disregarding values with letter or special characters")

# just for user effect, makes it feel cooler but completely unnecessary
# can be commented out
for i in range(0, 3):
    printUpdate()

# print total points to user
print("\n\nTotal Points:", avgScore)

# calculate average score
avgScore = avgScore/numDataLength

# display average score to user in percent
print("Average Score: ", avgScore, "%", sep="")

