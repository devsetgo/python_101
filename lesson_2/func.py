# Simple function to add values
def aFunction():
    a = 1
    b = 2
    c = a + b
    print(c)


# simple loop to count up in a range
def aLoop():
    count = 0
    # for each item in the range
    for item in range(0, 100):
        print(count)
        count = count + 1


# pass in a value below to aFunc, will fail if not an integer
def aFunc_1(my_num: int):

    result = aFunc_2(my_num)
    print(result)


# aFunc_2 will add 1 to var and then return the value of var to aFunc_1
def aFunc_2(var):
    var += 1
    return var


# If statement in a function. If a_lang is (==) a specific value then it prints a statement
def anIf(a_lang):
    if a_lang == "Python":
        print("cool")
    elif a_lang == "JAVA":
        print("not as cool as Python")
    else:
        print("You should have picked Python")


my_num: int = 10
language = "Python"

if __name__ == "__main__":
    # aFunction()
    # aLoop()
    aFunc_1(my_num)
    # anIf(language)
