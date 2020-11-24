print("Enter your grades for 5 classes")

class1 = int(input("What is your grade for Class 1? "))
class2 = int(input("What is your grade for Class 2? "))
class3 = int(input("What is your grade for Class 3? "))
class4 = int(input("What is your grade for Class 4? "))
class5 = int(input("What is your grade for Class 5? "))

if class1 < 0 or class2 < 0 or class3 < 0 or class4 < 0 or class5 < 0 or class1 > 100:
    print("Invalid input")

else:
    if class1 >= 90:
        class1 = 4
    elif class1 >= 80:
        class1 = 3
    elif class1 >= 70:
        class1 = 2
    elif class1 >= 60:
        class1 = 1
    else:
        class1 = 0

    if class2 >= 90:
        class2 = 4
    elif class2 >= 80:
        class2 = 3
    elif class2 >= 70:
        class2 = 2
    elif class2 >= 60:
        class2 = 1
    else:
        class2 = 0

    if class3 >= 90:
        class3 = 4
    elif class3 >= 80:
        class3 = 3
    elif class3 >= 70:
        class3 = 2
    elif class3 >= 60:
        class3 = 1
    else:
        class3 = 0

    if class4 >= 90:
        class4 = 4
    elif class4 >= 80:
        class4 = 3
    elif class4 >= 70:
        class4 = 2
    elif class4 >= 60:
        class4 = 1
    else:
        class4 = 0

    if class5 >= 90:
        class5 = 4
    elif class5 >= 80:
        class5 = 3
    elif class5 >= 70:
        class5 = 2
    elif class5 >= 60:
        class5 = 1
    else:
        class5 = 0

    gpa = (class1 + class2 + class3 + class4 + class5) / 5
    print("Your current GPA is " + str(gpa))