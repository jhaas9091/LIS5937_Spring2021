"""Module #5 Assignment
Julie Haas
LIS 5937
Spring 2021"""

"1. Write a Python program to execute a string containing Python code"

"Comparing Input Person to Tommy, Aged 10"
def compareage(name=str, age=int):
    def comparetommy(name, age):
        Tommy = 10
        if Tommy < age:
            return "Tommy is younger than " + name + " by " + str(age - Tommy) + " years."
        if Tommy > age:
            return "Tommy is older than " + name + " by " + str(Tommy - age) + " years."
        if Tommy == age:
            return "Tommy and " + name + " are the same age."
        else:
            return "There was a problem. Please try again."
    return comparetommy

test = compareage(str, int)
print(test("Anna", 3))
print(test("Robbie", 17))
print(test("Steve", 10))

"2. Write a Python function to insert a string in the middle of a string"

"Reporting weather input by user"
def weatherrep(str,weather):
    return str[:14] + " " + weather + " " + str[-5:]

print (weatherrep("The weather is __ today",'Cloudy'))
print (weatherrep("The weather is __ today",'Sunny'))
