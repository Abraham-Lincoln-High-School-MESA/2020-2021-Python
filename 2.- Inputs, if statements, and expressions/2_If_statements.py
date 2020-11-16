""" If statements are basically decisions the program can make depending on whether or not something is true
    meaning they have a condition, which is of boolean type
        if condition:
            do something
            do something

    Note that if the condition is not met, then the code inside just does not execute, and that in order
    for the statement to work all the code that is to be executed has to be indented with a tab (just press the tab key)
"""

wantCandy = input("Do you want a candy? (yes or no) ")
if wantCandy == "yes":                                                                  # If wantCandy is equal to "yes"
    print("Here you go\n")                                                              # Here you go

if 5 > 2:                                                                               # If 5 is greater than 2
    print("5 is greater than 2")                                                        # 5 is greater than 2

if 10 == 10:                                                                            # If 10 is equal to 10
    print("10 is equal to 10\n")                                                        # 10 is equal to 10

if 10 < 0:                                                                              # If 10 is less than 0
    print("10 is less than 0")                                                          # This will just not print as we know
                                                                                        # that the condition is not true

""" It also has an else statement (which is OPTIONAL to add), in which we execute something in case our original
    condition was not met (Note that you can only add ONE else and that it does not need a condition).
        if condition:
            do something
        else:
            do backup plan
"""

wantCandy = input("Do you want a candy? (yes or no) ")
if wantCandy == "yes":                                                                  # If wantCandy is equal to "yes"
    print("Here you go\n")                                                              # Here you go

else:                                                                                   # Else (if wantCandy is NOT True)
    print("Ok, see you next time\n")                                                    # Ok, see you next time

""" It has elif as well, which we use if we want to check more than one condition, and we can add as many as we want
        if number > 0:
            do task 1
        if number < 0:
            do task 2
        else:
            do task 3
"""

option = int(input("Input a number from 1 to 3: "))

if option == 1:                                                                         # If option is equal to 1
    print("Executing task 1...")                                                        # Executing task 1

elif option == 2:                                                                       # If option is equal to 2
    print("Executing task 2...")                                                        # Executing task 2

elif option == 3:                                                                       # If option is equal to 3
    print("Executing task 3...")                                                        # Executing task 3

else:                                                                                   # Else
    print("Not a valid option")                                                         # Not a valid option

# Note that whenever we have an else, if any of the conditions were met, the else statement will ALWAYS execute

