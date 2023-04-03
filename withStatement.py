# Opening and reading files
# if the object has __enter and __exit method it can be used along "with" statement
try:
    with open("main.py") as file, open("sample.txt") as target:
        text = file.read()
        text_new = target.read()
        print("File opened" + text_new)
except FileNotFoundError:
    print("File doesnt exist")

