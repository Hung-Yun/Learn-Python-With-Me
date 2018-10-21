
"""

Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list
returns (then prints) an appropriate boolean.

"""

def main():
    
    import numpy
    new_number = int(input("[Please enter a number to see if it's in the list.] "))
    the_list = numpy.random.randint(0,100,100)
    print(the_list)
    
    # I realized that we can use if and else in the statement of printing.
    # Very STRAIGHTFORWARD!
    print("In the list" if new_number in the_list else "Not in the list")

if __name__=="__main__":
    main()
    
