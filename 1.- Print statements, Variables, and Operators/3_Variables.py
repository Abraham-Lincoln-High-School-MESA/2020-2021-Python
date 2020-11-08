#   11/08/2020  @author: Giovanni B

""" Variables store data... and... that's really it

    In python (unlike in other languages) we do not have to specify the variable type, we only create
    it and assign it a value:
    variableName = value

    There are several rules we have to follow:
    variable names have to begin with a letter from the alphabet or an underscore
            variable_1  yes         1name   NO
    variable names are case sensitive
            variable1   and     vAriable1   are NOT the same
    variable names cannot be keywords
            printVariable   yes     print   NO

    These are not rules, but are nice to follow as they are non-written standards:
    variable names should ALWAYS start lowercase, we can use camelcase or underscores after
            variableNameNumber1 or variable_name_number_1  yes       Variable    NO
    Should be relevant to the value
            carModel = "Tesla Model x"  yes         variable1 = "Tesla Model x"     NO

    The most common variable types are strings, which is text in "quotes",
    booleans, which are True or False,
    and numbers, however, we have two different variable types to represent numbers,
    integers, which only hold integers, and floating, which can hold decimal points
"""

intVariable = 5 + 5 * 2                 # integer variable (numbers)
print(intVariable)                      # 15

stringVariable = "this is a variable"  # string variable (text; must be in "quotes")
print(stringVariable)                  # this is a variable

booleanVariable = 7 == 7               # boolean variable (True or False)
print(booleanVariable)                 # True

''' There might be times in which we need to convert a variable into another type, for that we
    need to cast a variable. The most common castings are: 
    str(), which converts into a string
    int(), which converts into an integer
    
    But why would we even need to cast them?
    Here are some examples
'''

stringChocolatePrice = "2"          # What if I want to know the price for 5 chocolates?
                                    # I cannot multiply text, so I cannot do stringChocolatePrice * 5
                                    # I can't do stuff with it :(

chocolatePrice = int(stringChocolatePrice)   # I can now do stuff with it :)
print(chocolatePrice * 5)                    # 10

# Note that when working with int() we have to make sure that the string we are trying to cast
# contains only numbers, for instance, "2739".
# If we did the same with a string containing non-digit characters we would get an error, for instance,
# int("not a number") >> ValueError: invalid literal for int() with base 10

age = 58
print("His age is " + str(age))             # His age is 58
                                            # We could also do:
string_Age = str(age)
print("His age is " + string_Age)           # His age is 58
