try:
    age = int(input("Enter Age:"))
except ValueError:
    print("You have entered wrong ")
# this is optional
else:
    print(f"I am printed if no error is thrown , your age is {age}")