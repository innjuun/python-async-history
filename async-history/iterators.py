# sum = 0
# for i in range(100000):
#     sum += i


class Counter(object):
    def __iter__(self):
        iter = Iterator()
        return iter

class Iterator(object):
    def __init__(self):
        self.index = 0

    def __next__(self):
        if self.index > 10:
            raise StopIteration
        n = self.index * 2
        self.index += 1
        return n

iterator = Counter()
next(iterator)
next(iterator)

iterator = Counter()
for i in iterator:
    print(i)