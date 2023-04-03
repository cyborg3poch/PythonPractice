# This expects any numbers of arguments
# all the normal argument is packed in args -> in a tuple
# all the key worded arguments are packed in kwargs -> in a dictionary
def show(*args, **kwargs):
    print(args, kwargs)


# defining lambda  function add
add = lambda a, b: a + b

if __name__ == '__main__':
    show("shivank", g="shivank")
