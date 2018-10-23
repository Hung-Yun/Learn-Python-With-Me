
"""

The user enters a cost and then the amount of money given.
The program will figure out the number of quarters, dimes, nickels, pennies needed for the change.

"""

def count(coin, rest_of_change):
    """Count the amount of coin with the rest of change for each coin"""
    count = 0
    while True:

        # I don't know how to deal with float number
        # If I set " rest_of_change - coin > 0 "
        # then cost = 0.07, given = 1 would give a wrong number of pennies
        if rest_of_change - coin > -0.001:
            rest_of_change -= coin
            count += 1
        else:
            break
    return count

def main():

    # Quarters = 0.25 / Dimes = 0.1 / Nickel = 0.05 / Pennies = 0.01
    change_dict = {}
    cost = float(input("Please enter the cost. "))
    given = float(input("Please enter the amount of money given "))
    change = given - cost

    def for_next_coin(change, coin, count):
        """should return the change for the next coin"""
        return change - coin * count

    change_dict["Quarters"] = count(0.25, change)
    change = for_next_coin(change, 0.25, count(0.25, change))
    change_dict["Dimes"] = count(0.1, change)
    change = for_next_coin(change, 0.1, count(0.1, change))
    change_dict["Nickel"] = count(0.05, change)
    change = for_next_coin(change, 0.05, count(0.05, change))
    change_dict["Pennies"] = count(0.01, change)
    change = for_next_coin(change, 0.01, count(0.01, change))
    print(change_dict)

if __name__=="__main__":
    main()
