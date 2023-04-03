# https://docs.python.org/3/library/exceptions.html#bltin-exceptions
def calculate_xfactor():
    try:
        file = open("main.py")
        age = int(input("Enter Age:"))
        x = 10 / age
    except (ValueError, ZeroDivisionError):
        print("You have entered wrong ")
    # this is optional
    else:
        print(f"I am printed if no error is thrown , your age is {age}")
    finally:
        file.close()


