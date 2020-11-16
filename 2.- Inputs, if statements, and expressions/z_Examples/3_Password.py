# I've set the password default to "admin"

password = "admin"
attempt = input("Please enter the password to access: ")

if attempt == password:
    print("Access Granted")
    print("Who do you wanna hack?")

else:
    print("Access Denied")
