
"""

Write a program that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
For example, say I type the string: "My name is Michele"
Then I would see the string: "Michele is name My." shown back to me.
I try to use other methods that are cleaner.

"""

def get_string(inp):
    return str(input(inp))

def store(string):
    """slice the input into different string and store it"""
    string_list = string.split(" ")
    new_string = " ".join(string_list[::-1])
    print(new_string)

if __name__=="__main__":
    store(get_string("[Give me a sentence] "))
    
