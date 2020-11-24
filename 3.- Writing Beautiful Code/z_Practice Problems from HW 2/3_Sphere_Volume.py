pi = 3.14159

r = int(input("What is the radius? "))

if r > 0:
    volume = (4 / 3) * pi * r**3
    print("The volume is " + str(volume))

else:
    print("Invalid input")
