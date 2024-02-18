# Python List comprehension provides a much more short
# syntax for creating a new list based on the values of an existing list.
# Syntax --> newList = [ expression(element) for element in oldList if condition ]

evenlist = [i for i in range(20) if i%2==0]
print(evenlist)
