print("hello")
print("this" + " " + "that")

# Simple print statements
a = 1
print(a)
b = 1
print(a + b)

# concantenation within a print statement. It requires non-string variables to be converted to a string
c = a + b
print(str(a) + " + " + str(b) + " = " + str(c))

# string formatting
print("{} + {} = {}".format(a, b, c))

# print a f string and math can be done within it
# f strings are only Python 3.6 and higher
x = f"{a} + {b} = {a + b}"
print(x)
