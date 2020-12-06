""" A list is basically an array of variables and/or values and yeah... that's it.
    However, as we know, it is more than the sum of its parts. By being having lists we are now
    able to order those values, interchange them, and get access to pretty cool methods and functions.

    We haven't covered this yet, but functions and methods are different, so a vague form of differentiating
    a function and a method is that:
    functions can usually be alone
    e.g --> sqrt(num)    len(list)   floor(num)

    while methods are "attached" to something else and need a period
    e.g --> listName.sort()     list3.index(element)    attendance.pop()

    Lists can hold values of any type, and can hold different types at the same time.
    There are several ways to declare lists, but the easiest one is by declaring it as an already known variable,
    using brackets [] to hold their values, and commas to separate them

    We call the data the lists hold, elements

    listName = ["Michael", 10, True, 0.5, "Giovanni", False]
"""

severalTypes = ["Michael", 10, True, 0.5, "Giovanni", False]
print(severalTypes)                                                 # ['Michael', 10, True, 0.5, 'Giovanni', False]

numbersOnly = [4, 7, 0, 10, 3]
print(numbersOnly)                                                  # [4, 7, 0, 10, 3]

stringsOnly = ["Names", "food", "items", "strings"]
print(stringsOnly)                                                  # ['Names', 'food', 'items', 'strings']
print()

""" One of several weird thing we do in programming (not only fo this language) is to start counting on 0,
    which applies not only to lists, but also loops, functions, counters, and so.
    
    Thus, we use:
    listName[index]
    
    To get an element at that specific index. So, if I want to, let's say, get the first
    element of my previously declared stringsOnly list, which is "Names", I would do
    stringsOnly[0]
    because we start counting from 0
"""

print(stringsOnly[0])                                           # Names
print(stringsOnly[1])                                           # food
print(stringsOnly[2])                                           # items
print(stringsOnly[3])                                           # strings
print()

""" So, as you can tell, even though there are 4 elements in my list, there is no such thing
    as stringsOnly[4], which will result in a IndexError: list index out of range.
    In a similar way, we can change the value of an specific index by
    listName[2] = newElement
    
    So if I wanted to change my second string in stringsOnly, which is food, to pencils, I would do
    stringsOnly[2] = "pencils"
"""

stringsOnly[2] = "pencils"
print(stringsOnly)                                              # ['Names', 'food', 'pencils', 'strings']
print()

""" Then we have the len() function, which basically gives us the list's length by
    len(listName)
    which if I used with my stringsOnly, would return 4
"""

print(len(stringsOnly))                                 # 4

# If I did not know my list length and wanted to print the last element I could do

print(severalTypes[len(severalTypes) - 1])              # False
print()

# len(severalTypes) is 6, so we have
# severalTypes[6 - 1]
# severalTypes[5] which is False

""" Python lists count with 11 useful methods:

    index(element)              Returns the index of the element
    append(element)             Adds the element at the end of the list
    insert(index, element)       Adds the element in the specified index and shifts all the elements after to the right
    pop() or pop(index)         Removes the last element if no index; else removes the element of the specified index
    remove(element)             Removes the specified element
    clear()                     Removes all items from the list
    sort()                      Sorts in ascending or alphabetical order
    count(element)              Returns the number of times the element appears on the list
    reverse()                   Reverses the list
    copy()                      Copies a list
    extend()                    Adds all the elements of an iterable (we'll explain this later)
    
    For more information in these methods: https://www.programiz.com/python-programming/methods/list
    
    The syntax we use is
    listName.method() 
    
    Finally we can also slice, which is, get a sublist by
    sublist = list[a:b]
    
    Where a is the firstElement we want and
    b is the lastElement + 1
"""

programmingLanguages = ["C++", "Python", "Java", "COBOL", "C#", "PHP"]

print(programmingLanguages.index("C++"))                                # 0

programmingLanguages.append("SQL")
print(programmingLanguages)                                             # ['C++', 'Python', 'Java', 'COBOL', 'C#', 'PHP', 'SQL']

programmingLanguages.insert(3, "Visual Basic")
print(programmingLanguages)                                             # ['C++', 'Python', 'Java', 'Visual Basic', 'COBOL', 'C#', 'PHP', 'SQL']

programmingLanguages.pop()
print(programmingLanguages)                                             # ['C++', 'Python', 'Java', 'Visual Basic', 'COBOL', 'C#', 'PHP']

programmingLanguages.pop(4)
print(programmingLanguages)                                             # ['C++', 'Python', 'Java', 'Visual Basic', 'C#', 'PHP']

programmingLanguages.remove("C#")
print(programmingLanguages)                                             # ['C++', 'Python', 'Java', 'Visual Basic', 'PHP']

copy = programmingLanguages.copy()
print(copy)                                                             # ['C++', 'Python', 'Java', 'Visual Basic', 'PHP']

copy.sort()
print(copy)                                                             # ['C++', 'Java', 'PHP', 'Python', 'Visual Basic']

print(copy.count("C++"))                                                # 1

copy.reverse()
print(copy)                                                             # ['Visual Basic', 'Python', 'PHP', 'Java', 'C++']

copy.clear()
print(copy)                                                             # []
