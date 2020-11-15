raining = input("Is it raining? ")

# Ignore this, this is the behind the scenes to convert a yes to True and a no to False
if raining == "yes":
    raining = True
else:
    raining = False

# This is what matters
if not raining:
    print("You do not need an umbrella")

else:
    print("You need an umbrella")
