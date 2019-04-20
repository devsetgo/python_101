from func import aFunc_1, anIf

# pass a value to function in another file
my_number = 100
aFunc_1(my_number)

# pass a value to a funcation in another file
language = "Python"  # 'Python' 'C++' 'JAVA'
anIf(language)


# more objected oriented way of making a function
# imaging a simple math function to deal with 2 numbers
# and add, subtract, multiple or divide
from mathFunc import mathFunction

value_1 = 1
value_2 = 10
want = "add"  # add, sub, mult, div
result = mathFunction(value_1, value_2, want)
print(result)
