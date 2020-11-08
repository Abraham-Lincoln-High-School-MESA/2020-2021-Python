#   11/08/2020  @author: Giovanni B

""" Operators are symbols that tell the compiler to perform certain mathematical of logical manipulations.
    For instance, arithmetic, comparison, boolean, etc. There are several operators, and they obviously
    have a precedence order, this is, the order of "importance" to decide which one to perform first,
    for which I added an image into the folder that explains it.
    PD: In the image they forgot to add the parenthesis, which have the highest precedence

    Most of the operators are used for integer and boolean operations, the only notable exception would
    be that besides to sum integers, we can use the + operator to concatenate strings, this is, to
    join them   """

# String operators
print("Concatenating " + "strings")                 # Concatenating strings

# All of the following are integer operators
print(5 + 10)                                       # 15; Summing
print(10 - 2)                                       # 8;  subtracting
print(30 / 3)                                       # 10; dividing
print(7 * 9)                                        # 63; multiplying

x = 8                                               # We can also use operators with variables
y = 17
print(x - y)                                        # -9; subtracting
print(x + y)                                        # 25; subtracting

print(9 % 4)                                        # 1;  reminder of the division
print(8 ** 2)                                       # 64; to the power

# All of the following are boolean operators
print(5 == 5)                                       # True;     is 5 equal to 5?
print(6 == 0)                                       # False;    is 6 equal to 0?
print(4 != 0)                                       # True;     is 4 not equal to 0?
print(5 != 5)                                       # False;    is 5 not equal to 5?

print(10 > 10)                                      # False;    is 10 greater than 10?
print(10 >= 10)                                     # True;     is 10 greater than or equal to 10?
print(7 < 10)                                       # True;     is 7 less than 10?
print(7 <= 7)                                       # True;     is 7 less than or equal to 7?

# We can also "mix" integer and boolean operators
print(10 > (2 * 3))                                   # True;     is 10 greater than 6 (2 * 3)?
print(10 == (5 * 2))                                  # True;     is 10 equal to 10 (5 * 2)?



