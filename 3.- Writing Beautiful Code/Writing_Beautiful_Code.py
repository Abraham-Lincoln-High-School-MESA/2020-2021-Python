""" Because programming is a technical profession, we often approach it without thought to design.

    Code is for getting a computer to do what we need, why should design matter?

    - Better use of your time
    - It is easier to read
    - Quickly digestible and easy to extend
    - Easier to debug (find errors)

    Here are some code guidelines and tips to write beautiful code

    """

# Code "separation"
from math import pi                             # We ALWAYS put imports first


def printSomething():                           # Functions
    print("something")


radius = 4                                      # Declaring KNOWN variables

height = int(input("Input the height: "))       # Rest of the code below
# Code
# Code

volume = pi * radius ** 2 * height

# ---------------------------------------------

#                                  Inputs
# There should be one space between the input statement and the user’s input

name = input("What is your name?")	    # Do not

name = input("What is your name? ")	    # Do

# ---------------------------------------------

#                                   Operators
# There should be spaces between operators

h = 5
r = 2

volume_cone = pi*r**2*h/3						    # Do not

volume_cone = pi * r**2 * (h / 3)					# Do

if r==9:											# Do not
    print("r is 9")

if r == 9:											# Do
    print("r is 9")

# ----------------------------------------------

#                                   Indentations
# Python uses 4 spaces as indentation by default (the same as a tab)
# Not only for if’s. I do not know why repl.it only does 2.

option = input("Input an option: ")

if option == 1:										# Do not
  print("Executing task 1")

if option == 1:										# Do
    print("Executing task 1")

# ----------------------------------------------

#                               Comments Indentations
# Should be at least 2 spaces after code
# Should have one space between the # and the comment

print("Hello world")#prints something				    Do not


print("Hello world")  # prints something				Do

print("Hello world")  			    # prints something	Do


