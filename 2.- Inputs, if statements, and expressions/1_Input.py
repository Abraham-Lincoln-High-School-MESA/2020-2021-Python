""" We use input to let the User enter data that can be converted into almost if not any
    type. This way we can make our program give us different outputs as the inputs change.
    Logging into an account, entering a card PIN, calculators, keyboards, cellphones, computers
    videogames, joysticks, buttons, and almost all electronic devices are examples of things
    that need the User (a person) to input information.
    You could even say that pressing the power button itself is a kind of input, as
    the device needs you to do it, so it can work.

    Let us say we have a watering system for the grass that waters it everyday when sun rises.
    Even in this case the system does need an input, from a light sensor, telling it is time to water,
    however in this case we do not need you as a person telling it to do so. This is an automated process.
"""

# Whenever we input something it is ALWAYS stored as a string variable
name = input("What is your name? ")
print("Nice to meet you " + name + "\n")                                                        # Nice to meet you ^name

# So if we need a different type of variable we need to cast it
# This is for ints
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
print(str(num1) + " plus " + str(num2) + " is equal to " + str(num1 + num2) + "\n")             # ^num1 plus ^num2 is equal to ^(num1 + num2)

# With booleans, any string that is not empty, and any number that is not 0, are True

adult = bool(input("Are you an adult? (leave empty for False, write something for True): "))    # This is how we convert a string to boolean
likeLA = bool(int(input("Do you like LA? (0 for False, 1 for True): ")))                        # This is how we convert a string to int and then to bool
print("It is " + str(adult) + " that you are an adult")                                         # It is ^adult
print("It is " + str(likeLA) + " that you like LA")                                             # It is ^likeLA

# We can create infinite number of things with inputs, as far as our imagination wants
# While print() is how the computer talks to us, input() is how we talk to the computer


