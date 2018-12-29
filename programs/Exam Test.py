def main():
    money = input("Enter the numerical equivalent for currency: ")
    print(convertMoney(money))

def convertMoney(money):
    if (money == ".01"):
        return "Penny"

    elif (money == ".05"):
        return "Nickel"

    elif (money == ".10"):
        return "Dime"

    elif (money == ".25"):
        return "Quarter"

    elif (money == "1.00"):
        return "Dollar"

    elif (money == "5.00"):
        return "Five Dollar"

    elif (money == "10.00"):
        return "Ten Dollar"

    elif (money == "20.00"):
        return "Twenty Dollar"

    elif (money == "50.00"):
        return "Fifty Dollar"

    elif (money == "100.00"):
        return "One Hundred Dollar"

    else:
        return "ValueError: Incorrect Input"

main()
