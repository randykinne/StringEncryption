# Randy Kinne
# Program 4
# COMS-170-WWW01: Fall 2017
# Due: 10/09/2017
# Compound Interest Calculator
# ------------------------------------------------------------------
# Variable              Type            Purpose
# ------------------------------------------------------------------
# Decimal               Decimal         Easier to reference decimal.Decimal
# principal             Decimal         Value of principal investment
# rate                  String/Decimal  Value of annual interest rate
# time                  Integer         Value of time in years default value is 5
# balance               Decimal         Value of balance after other variables calculated together

# Importing decimal to use it, declaring it as Decimal to make it easier to call
import decimal
Decimal = decimal.Decimal

# Variables store data collected from user input
principal = Decimal(input("What is the dollar value of your deposit? ").replace("$", ""))
rate = input("What percent value is your annual interest rate? ").replace("%","")

# Converts percentage to decimal, then rounds to 2 places
rate = round(Decimal(Decimal(rate) / 100), 2)

# Default time is 5 years
time = 5

# Formula for compound interest is Principal*(1+Rate/times_per_year)^(times_per_year*years)
for x in range(time):
    x+=1
    balance = principal*((1+(rate)) ** x)
    # Comment out line below to test looping
    # print("Balance: ", balance)

# Print output to user
print("Your balance after ", time, " years would be: $", round(balance, 2), sep="")
# Smaller version of the same entire calculation above: balance = round(principal*pow((1+(rate)), time), 2)

# End of program

##Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
##[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
##Type "copyright", "credits" or "license()" for more information.
##>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
##Visit http://www.python.org/download/mac/tcltk/ for current information.
##
##======== RESTART: /Users/randykinne/Documents/School/2017/Program4.py ========
##What is the dollar value of your deposit? $50
##What percent value is your annual interest rate? 5%
##Your balance after 5 years would be: $63.81
##>>> 
