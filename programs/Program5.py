# Randy Kinne
# Program 5
# COMS-170-WWW01: Fall 2017
# Due: 10/30/2017
# Product Order Price Calculator
# ------------------------------------------------------------------
# Variable              Type            Purpose
# ------------------------------------------------------------------
# Decimal               Decimal         Easier to reference decimal.Decimal
# subTotal              Decimal         Storing the user's subtotal and passing
# shipping              Decimal         Storing the user's shipping costs
# handling              Decimal         Storing the user's handling costs
# tax                   Decimal         User's tax costs
# grandTotal            Decimal         user's grand total, all values added up-01

# Import decimal to use it and declare Decimal to make it easier to reference
import decimal
Decimal = decimal.Decimal

# Function getSubtotal asks user for their subtotal, verifies it, and returns it
def getSubTotal():
    subTotal = Decimal(input("Please enter your subtotal: ").replace("$",""))
    while (subTotal < 1 or subTotal > 9999):
        print("Please enter an amount between $1-$9,999")
        subTotal = Decimal(input("Please enter your subtotal: ").replace("$",""))
    return subTotal

# Function calculateCosts switches between returning shipping and handling
# based on boolean value of handling, then calculates shipping or handling
# and then returns it to main
def calculateCosts(subTotal, handling):
    if (handling is True):
        if (subTotal < 100):
            return Decimal(2)
        else:
            return Decimal(0)
    else:
        shipping = subTotal * Decimal(0.1) # 10%
        return Decimal(shipping)

# Function calculateTax calculates sales tax and returns it to main
def calculateTax(subTotal):
    return subTotal * Decimal(0.06) # 6%

# Function main calls all of the functions above and uses their results to pass
# variables to the next functions, then prints the totals
def main():
    subTotal = Decimal(getSubTotal())
    shipping = calculateCosts(subTotal, False)
    handling = calculateCosts(subTotal, True)
    tax = calculateTax(subTotal)
    grandTotal = subTotal + shipping + handling + tax

    print("Product Total Information")
    print("Subtotal: $", round(subTotal, 2), sep="")
    print("Shipping: $", round(shipping, 2), sep="")
    print("Handling: $", round(handling, 2), sep="")
    print("Sales Tax: $", round(tax, 2), sep="")
    print("Grand Total: $", round(grandTotal, 2), sep="")

main()

# End of program

##Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
##[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
##Type "copyright", "credits" or "license()" for more information.
##>>> 
##======== RESTART: /Users/randykinne/Documents/School/2017/Program5.py ========
##Please enter your subtotal: 0
##Please enter an amount between $1-$9,999
##Please enter your subtotal: 100
##Product Total Information
##Subtotal: $100.00
##Shipping: $10.00
##Handling: $0.00
##Sales Tax: $6.00
##Grand Total: $116.00
##>>> 
