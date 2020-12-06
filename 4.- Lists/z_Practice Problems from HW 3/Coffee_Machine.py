# Initializing variables
waterPerCup = 0
milkPerCup = 0
beansPerCup = 0
costPerCup = 0

# Inputting the resources
print("Enter the machine's resources")

water = int(input("ml of water: "))
milk = int(input("ml of milk: "))
beans = int(input("gr of coffee beans: "))
cups = int(input("cups: "))
money = int(input("How much do you have? $"))

# Selecting a coffee
print("What do you want to buy?")
print("1.- Espresso $4\n2.- Latte $7\n3.- Cappuccino $6")

option = int(input())

# Assigning the needed resources
if option == 1:

    waterPerCup = 250
    milkPerCup = 0
    beansPerCup = 16
    costPerCup = 4

elif option == 2:

    waterPerCup = 350
    milkPerCup = 75
    beansPerCup = 20
    costPerCup = 7

elif option == 3:

    waterPerCup = 200
    milkPerCup = 100
    beansPerCup = 12
    costPerCup = 6

# Inputting the number of cups
cupsOfCoffee = int(input("How many cups would you like? "))

# Calculating the maximum of coffee cups we can make
min = water // waterPerCup

if milkPerCup != 0 and milk // milkPerCup < min:
    min = milk // milkPerCup

if beans // beansPerCup < min:
    min = beans // beansPerCup

if money // costPerCup < min:
    min = money // costPerCup

if cups < min:
    min = cups


# Choosing what message to display
if min == cupsOfCoffee:
    print("Here you go!")

elif min < cupsOfCoffee:
    print("I can only make " + str(min) + " cups")

elif min > cupsOfCoffee:
    print("I can even make " + str(min) + " cups")
