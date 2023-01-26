class MyDict:
    def __init__(self):
        self.dict = dict()

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __getitem__(self, key):
        return self.dict[key]

    def get(self, key, default):
        return self.dict.get(key, default)

    def __iter__(self):
        return iter(self.dict)

    def __str__(self):
        return str(self.dict)


dict1 = MyDict()
print(dict1)
dict1["key1"] = 1
dict1["key2"] = 2
dict1["key1"] = "one"
print(dict1)
print(dict1["key2"])
print(dict1.get("key1", 2))
print(dict1.get("key2", 1))
print(dict1.get("key3", "default value"))

for i, v in enumerate(dict1):
    print(i, v)