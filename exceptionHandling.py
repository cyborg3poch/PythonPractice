def calculate_xfactor():
    age = int(input("Enter your age :"))
    if age <= -1:
        raise ValueError("Age can't be lower than 0")
    elif type(age) != type(1):
        raise ValueError("age cant be a string or char")
    else:
        print(f"You are {age} year old!")


try:
    calculate_xfactor()
except ValueError as ex:
    print(ex)
