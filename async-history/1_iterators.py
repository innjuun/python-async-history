# sum = 0
# for i in range(100000):
#     sum += i


# Iterable(iterator 객체를 생성할 수있다!)
class Counter(object):
    def __iter__(self):
        iter = Iterator()
        return iter

# Iterator(__next__()를 구현해서 순환하는 다음 값을 반환한다!)
class Iterator(object):
    def __init__(self):
        self.index = 0

    def __next__(self):
        if self.index > 10:
            raise StopIteration
        n = self.index * 2
        self.index += 1
        return n


iterator = iter(Counter())
print(next(iterator))
print(next(iterator))


iterator = Counter()
for i in iterator:
    print(i)