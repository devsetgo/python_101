# example function


def mathFunction(value1: float, value2: float, want: str):
    # type of math 'want' we will support in ths function
    math_types = ["add", "sub", "mult", "div"]

    # if it is not a supported type, return the error
    if want not in math_types:
        result = "not a currently support math type"

    elif want == "add":
        # simple addition
        result = value1 + value2

    elif want == "sub":
        # simple subtraction
        result = value1 - value2

    elif want == "mult":
        # simple multiplication
        result = value1 * value2

    elif want == "div":

        # this is an error handling block
        # you cannot divide by zero as it is not possible in math
        try:
            # simple division
            result = value1 / value2
        except ZeroDivisionError as error:
            # error handling of divide by zero
            result = f"Error: {error}"

    # return the result from above
    return result


# lets run through a function that is a bit more objected oriented
math_types = ["add", "sub", "mult", "div", "remainder"]
for item in math_types:
    value_1 = 10000  # set value as float or integer
    value_2 = 0  # set value as float or integer and try a 0 here to see error handling
    w = item  # math_type item in list
    my_answer = mathFunction(value_1, value_2, w)  # call function with variables
    print(my_answer)  # return value of result in function
