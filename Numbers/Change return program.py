
"""

The user enters a cost and then the amount of money given.
The program will figure out the number of quarters, dimes, nickels, pennies needed for the change.

"""

def main():

    # Quarters = 0.25 / Dimes = 0.1 / Nickel = 0.05 / Pennies = 0.01
    change_info = {}
    cost = float(input("Please enter the cost. "))
    given = float(input("Please enter the amount of money given "))
    change = given - cost
    change_info["Quarters"] = int(change/0.25)
    change -= change_info["Quarters"] * 0.25
    change_info["Dimes"] = int(change/0.1)
    change -= change_info["Dimes"] * 0.1
    change_info["Nickel"] = int(change/0.05)
    change -= change_info["Nickel"] * 0.05
    change_info["Pennies"] = int(round(change,2)/0.01)
    print(change_info)
    
if __name__=="__main__":
    main()
