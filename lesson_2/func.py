# Simple function to add values
def aFunction():
    a = 1
    b = 2
    c = a + b
    print(c)
    return c


# simple loop to count up in a range
def aLoop():
    count = 0
    # for each item in the range
    for item in range(0, 100):
        print(count)
        count = count + 1

    return count

# pass in a value below to aFunc, will fail if not an integer
def aFunc_1(my_num: int):

    result = aFunc_2(my_num)
    print(result)
    return result


# aFunc_2 will add 1 to var and then return the value of var to aFunc_1
def aFunc_2(var):
    var += 1
    return var


# If statement in a function. If a_lang is (==) a specific value then it prints a statement
def anIf(a_lang):
    if a_lang == "Python":
        result = 'cool'
        print(result)
    elif a_lang == "JAVA":
        result = 'not as cool as Python'
        print(result)
    else:
        result = 'You should have picked Python'
        print(result)

    return result

my_num: int = 10
language = "Python"

if __name__ == "__main__":
    # aFunction()
    aLoop()
    # aFunc_1(my_num)
    # anIf(language)
