option = int(input("Select an option between 1 and 3: "))

if option == 1:
    print("Executing task 1")

elif option == 2:
    print("Executing task 2")

elif option == 3                            # Missing colon :
    print("Executing task 3")

else option > 3:                            # Else must have no condition
    print("Not a valid option")
