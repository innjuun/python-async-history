# def coro1():
#     print('C1: Start')
#     yield
#     print('C1: a')
#     yield
#     print('C1: b')
#     yield
#     print('C1: end')

# def coro2():
#     print('C2: Start')
#     yield
#     print('C2: a')
#     yield
#     print('C2: b')
#     yield
#     print('C2: end')

# def run(coros):
#     coros = list(coros)

#     while coros:
#         for coro in list(coros):
#             try:
#                 coro.send(None)
#             except StopIteration:
#                 coros.remove(coro)

# c1 = coro1()
# c2 = coro2()
# run([c1, c2])

import types

@types.coroutine
def switch():
    yield

async def coro1():
    print('C1: Start')
    await switch()
    print('C1: a')
    await switch()
    print('C1: b')
    await switch()
    print('C1: end')

async def coro2():
    print('C2: Start')
    await switch()
    print('C2: a')
    await switch()
    print('C2: b')
    await switch()
    print('C2: end')

def run(coros):
    coros = list(coros)

    while coros:
        for coro in list(coros):
            try:
                coro.send(None)
            except StopIteration:
                coros.remove(coro)

c1 = coro1()
c2 = coro2()
run([c1, c2])