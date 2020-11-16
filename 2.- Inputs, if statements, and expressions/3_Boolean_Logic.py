""" Boolean Logic is a form of algebra which is centered around three simple words known as
    Boolean Operators: “OR,” “AND,” and “NOT”. These three are the simplest and also the main logic gates
    there are. By combining this we can make much more complex gates, but we don't have to worry about those... yet.
    At the heart of Boolean Logic is the idea that all values are either true or false.

    The word binary is in the same word family as boolean is.
    Binary comes from the late Latin bīnārius, which means “consisting of two,” the idea on which this logic works
    Boolean values can have several "names" depending on the language or the abstraction, but all of them have the same logic,
    the idea that there are only two values, and that one is "something" while the other is "nothing"

    This is way we can say boolean values are:
    1 or 0, True or False, High or Low, On or Off

    Logic gates were originally created as physical real objects, used in electronics, in which by wiring
    switches in a specific way, we could get a gate. This is why all truth tables are represented with
    1's and 0's instead of True's and False's

    True = 1            False = 0

    Needs at least one value            Needs both values               Just inverts the input
    to be true                          to be True

             OR                              AND                                 NOT
         0 0     0                        0 0     0                            0     1
         0 1     1                        0 1     0                            1     0
         1 0     1                        1 0     0
         1 1     1                        1 1     1
"""

haveMoney = input("Do you have money? (yes or no): ")
borrowMoney = input("Can someone lend you money? (yes or no): ")

if haveMoney == "yes" or borrowMoney == "yes":              # If you have money OR someone can lend you money; we at least need one to be true
    print("You can get a chocolate!\n")                     # You can get a chocolate

else:                                                       # If you do not have money, and no one can lend you money
    print("You can't get a chocolate :(\n")                 # You can't get a chocolate :(

wannaParty = input("Do you want to go to the party? (yes or no): ")
parentPermission = input("Do you have your parents permission? (yes or no): ")

if wannaParty == "yes" and parentPermission == "yes":       # If you want to go to the party AND you have your parents permission; we need both to be true
    print("Party time B)\n")                                # Party time B)

else:                                                       # If you do not want to go to the party or you don't have your parents permission
    print("No party :(\n")                                  # No party :(

num = int(input("Enter a number"))
if not num >= 10:                                           # If num is not greater or equal than 10
    print("The number is less than 10: ")                   # The number is less than 10
