# Often, when dealing with iterators, we also get need to keep a count of iterations. Python eases the programmers’
# task by providing a built-in function enumerate() for this task. Enumerate() method adds a counter to an iterable
# and returns it in a form of enumerating object. This enumerated object can then be used directly for loops or
# converted into a list of tuples using the list() function.


list_food = ["banana","apple","kiwi"]
print ("Return type:", type(enumerate(list_food)))
print(list(enumerate(list_food)))