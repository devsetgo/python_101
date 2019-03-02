# List is an array of values
aList = ["hi", "seven", 7, "bob"]
print(aList)
print(f"the second value in the list is: {aList[1]}")

# A dictionary is a key: value pair
aDictionary = {"name": "mike", "age": 48}

print(aDictionary)

# Reference a specific key: value
print(aDictionary["name"], aDictionary["age"])

# aDictionary['age'] is an integer and needs to be converted to string to print the concantenation
print(f"{aDictionary['name']} is {aDictionary['age']}")
