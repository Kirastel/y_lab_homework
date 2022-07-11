class CyclicIterator:

    def __init__(self, collection):
        self.collection = list(collection)
        self.length = len(self.collection)
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.length - 1:
            self.i += 1
            return self.collection[self.i]
        else:
            self.i = 0
            return self.collection[self.i]


cyclic_iterator = CyclicIterator(['one', 'two', 'three', 'four'])
for i in cyclic_iterator:
    print(i)




