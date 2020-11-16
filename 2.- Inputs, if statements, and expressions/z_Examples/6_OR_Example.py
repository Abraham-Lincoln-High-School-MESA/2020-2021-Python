print("Welcome to the subscribe page for our magazine")
adult = input("Are you 18 years or older? ")
parentConsent = input("Do you have parent consent? ")

# Ignore this, this is the behind the scenes to convert a yes to True and a no to False

if adult == "yes":
    adult = True
else:
    adult = False

if parentConsent == "yes":
    parentConsent = True
else:
    parentConsent = False

# This is what matters
if adult or parentConsent:                      # We only need ONE condition to be true
    print("\nCongrats, you are now subscribed")
else:
    print("\nSorry, you can't subscribe")

