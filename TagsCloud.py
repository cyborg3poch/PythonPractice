class TagCloud:
    def __init__(self):
        # initialise an empty dictionary on object creation
        # making tags private by adding "__" -> (__tags)
        self.__tags = {}

    def add(self, key):
        # self.tags.get(key, 0) --> returns value at key if present else 0
        self.__tags[key.lower()] = self.__tags.get(key.lower(), 0) + 1

    def __getitem__(self, key):
        return self.__tags[key.lower()]

    def __setitem__(self, key, value):
        self.__tags[key.lower()] = value

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        iter(self.__tags)


tc = TagCloud()
tc.add("shivank")
tc.add("Shivank")
tc.add("shivank")
# print(tc.__tags) ----> this wont work

#workaround ---> hack
print(tc._TagCloud__tags)
