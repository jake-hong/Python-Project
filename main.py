class Iterator:
    def __init__(self, sequence):
        self.idx = 0
        self.data = sequence

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        try:

            return self.data[self.idx - 1]

        except IndexError:
            self.idx = 0
            raise StopIteration


class Iterable:
    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        return Iterator(self.sequence)


iterator = Iterable("123").__iter__()


print(type(iterator))
print(iterator)
print(iterator.__next__())
print(iterator.__next__())

print(iterator.__next__())
