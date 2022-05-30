"""
Exercise 2A

I am writing a version of the sum funciton in python
The sum funtion takes an iterable argument and an optional second argument that is the starting.

"""

def mysum(*numbers, beginning = 0):
    sum = 0
    for x in numbers:
        sum += x
    return sum + beginning

print(mysum(*[1, 3, 5], 10))
print(mysum(*[1, 3, 5]))
print(mysum(1, 2, 3, 4))