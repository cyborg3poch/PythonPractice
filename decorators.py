users = {
    "shivank": "pass",
    "mayank": "123"
}


# This function receives a function as a parameter and then calls it if a condition is fulfilled
def login_required(func):
    def wrapper(username, password, *args, **kwargs):
        if username in users and users[username] == password:
            # Adding a start so that tuple is inflated
            func(*args)
        else:
            print("Not Authenticated")

    return wrapper


# protected_add = login_required(add)

# protected_add("shivank", "pass", 2, 5)

# this thing is same as the decorator used
# add = login_required(add)

@login_required
def add(a, b):
    print(a + b)


add("shivank", "pass", 5, 8)
