pricePerMeal = 22
s = int(input("How many seniors are there? "))
a = int(input("How many adults? "))
c = int(input("How many children? "))

price = pricePerMeal * (0.5 * s + a)

if c < 3:
    price += pricePerMeal * c

tip = 0.15 * price

print("The price would be $" + str(price))
print("The tip would be $" + str(tip))
print("The total amount would be $" + str(price + tip))
