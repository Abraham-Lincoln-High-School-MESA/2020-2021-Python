#   11/08/2020  @author: Giovanni B

"""   The print statement literary prints text (more specifically strings) in the console,
      and is the main way in which the code communicates with the user/programmer
      Also, these three double quotes are how you make a multiple line comment :)
      (you can also use three single quotes)    """

# Here are several statements you can try your own!

print("Hello World!")                              # Hello World!
print("Any text you want")                         # Any text you want
print(5 + 4)                                       # 9

word = "Printing a variable!"
print(word)                                        # Printing a variable!

x = 498
print(x)                                           # 498

print(5 == 5)                                      # True
print(10 > 5)                                      # True
print(10 < 5)                                      # False

print("Concatenating" + " " + "text")              # Concatenating text

text = "Concatenating " + "text in a " + "variable!"
print(text)                                             # Concatenating text in a variable!

word1 = "Concatenating "
word2 = "several "
word3 = "variables"
print(word1 + word2 + word3 + ", how crazy is that!!")  # Concatenating several variables, how crazy is that!!

''' As we have seen so far, we can print almost every type of variable, string, integer, or boolean
    with the print statement. However, this is only true if in our print statement everything inside
    is of the same variable type, for instance:
    
    print("hi")       Works         print("hi" + 5 + 7)    Does not work :(
    print(4 + 6)      Works         print(5 + 7 + 5 == 5)  Does not work :(
    print(5 == 5)     Works
    
    So how do we print different types of variables?
    Easy, in these cases we have to cast all variables to string type, using str()
    (except for "everything in quotes" as that is already of the string type    '''

print("This is how " + str(5 + 10) + " " + str(10 > 5))  # This is how 15 True
print(str(5) + " times " + str(4) + " is equal to " + str(5 * 4))   # 5 times 4 is equal to 20

''' Finally, a very important component of the print statements are escape characters.
    An escape character is a combination of characters that has a meaning other 
    than the literal characters contained therein. This mean these characters have a
    specific function other than being printed.
    
    The most common escape characters are /n, which inserts a line break, and /t which inserts a tab '''

print("\nStanzas\nusually\nhave\n4 lines\n")
'''                                                     Stanzas
                                                        usually
                                                        have
                                                        4 lines '''

print("We can add as many\n\n\nline breaks as we want\n")
'''                                                     We can add as many


                                                        line breaks as we want '''

print("Also\t\ttabs")                                   # Also		tabs
