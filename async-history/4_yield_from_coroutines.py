# Case of calling coroutine from coroutine !!
# It is okay if the routine doesn't want to send data to the subroutines.
def subcoroutine():
    yield 1
    yield 2

def coroutine():
    for v in subcoroutine():
        yield v

x = coroutine()
print(next(x))    # 1 출력
print(next(x))    # 2 출력
# next(x)           # StopIteration


# How to send data to subcoroutine?
def subcoroutine():
    print("Subcoroutine")
    x = yield 1
    print("Recv: " + str(x))
    x = yield 2
    print("Recv: " + str(x))

# first way
def coroutine():
    _i = subcoroutine()
    _x = next(_i)
    while True:
        _s = yield _x
        _x = _i.send(_s)


x = coroutine()
print(next(x))
print(x.send(10))
# print(x.send(20))  # stopiteration

# send(None) == next(),
# but send(None) is only specific for generator, not iterator!

# second way, brilliant!
def yield_from_coroutine():
    yield from subcoroutine()

x = yield_from_coroutine()
print(next(x))
print(x.send(10))
# print(x.send(20))

# def returning_coroutine():
#     yield 1
#     e = StopIteration()
#     e.value = 10
#     raise e
def returning_coroutine():
    yield 1
    return 10

x = returning_coroutine()
next(x)
# next(x) # StopIteration

def sum(maximum):
    total = 0
    for i in range(maximum):
        total += i
        yield total
    return total
    # e = StopIteration()
    # e.value = 10
    # raise e

def coroutine(maximum):
    total = yield from sum(maximum)
    print(f"total: {total}")

coro = coroutine(10)
for c in coro:
    print(c)