# Randy Kinne
# Program 6
# COMS-170-WWW01: Fall 2017
# Due: 11/6/2017
# Program: File Number Reader
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# avgScore              Integer      Average Score 
# numDataLength         Integer      Number of scores added together, used to find average
#
# ------------------------------------------------------------------
# Function              Return Type     Purpose
# ------------------------------------------------------------------
# printUpdate()              N/A        Prints message for user, to make it seem like it's doing something

# import modules
import time
import sys

def printUpdate(x):
    for i in range(0, x):
        time.sleep(0.5)
        print(".", end="")

# verbose messages for user to see, added timings for user effect
print("Opening file numdata.txt", end="")
printUpdate(3)

# Open file numdata.txt, if it doesn't exist IOError exception is raised
try:
    f = open("numdata.txt")
except:
    print("\nIOError Exception: File numdata.txt not found!")
    print("\nMake sure the file name is spelled correctly and \nit is in the same location as this program and try again.")
    sys.exit() # quit program

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
            print("Disregarding lines with letters or special characters")

# just for user effect, makes it feel cooler but completely unnecessary
# can be commented out
printUpdate(3)

# print total points to user
print("\n\nTotal Points:", avgScore)

# calculate average score
avgScore = avgScore/numDataLength

# display average score to user in percent
print("Average Score: ", avgScore, "%", sep="")

# End of program

##Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
##[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
##Type "copyright", "credits" or "license()" for more information.
##>>> 
##== RESTART: /Users/randykinne/Documents/School/2017/Programming/Program6.py ==
##Opening file numdata.txt...
##
##numdata.txt found!
##
##Reading file numData.txt...
##
##Total Points: 684
##Average Score: 85.5%
##>>> 
