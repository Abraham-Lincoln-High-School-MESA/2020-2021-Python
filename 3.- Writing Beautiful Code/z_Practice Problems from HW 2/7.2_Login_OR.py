print("Input the Username and the PIN")

username = input("Username: ")
pin = int(input("PIN: "))

if username != "MESA_admin" or pin != 2570:
    print("Invalid credentials")
    print("One last chance")
    username = input("Username: ")
    pin = int(input("PIN: "))

    if username != "MESA_admin" or pin != 2570:
        print("Access DENIED")

    else:
        print("Access GRANTED")
else:
    print("Access GRANTED")
