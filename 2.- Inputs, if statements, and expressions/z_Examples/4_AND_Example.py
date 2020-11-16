interested = input("Do you want to subscribe to our magazine? ")
parentConsent = input("Do you have parent consent? ")

# Ignore this, this is the behind the scenes to convert a yes to True and a no to False

if interested == "yes":
    interested = True
else:
    interested = False

if parentConsent == "yes":
    parentConsent = True
else:
    parentConsent = False

# This is what matters
if interested and parentConsent:                    # We need BOTH conditions to be true
    print("\nCongrats, you are now subscribed")
else:
    print("\nSorry, you can't subscribe")

