def lightweight_coroutine():
    print('print 1')
    yield 1
    print('print 2')
    yield 2

generator = lightweight_coroutine()
type(generator)
dir(generator)
next(generator)
next(generator)
# next(generator)  Stopiteration


def before_generator_comprehension():
    for i in range(10):
        yield i * 2
# generator comprehension (lightweight coroutine)
# [x * 2 for x in range(10)]
generator = (x * 2 for x in range(10))

for g in generator:
    print(g)


# complicated? yields ! (lightweight coroutine)
def complicated_yield_generator():
    try:
        yield 1
        try:
            yield 2
            x = 1/0
            yield 3  # never get here
        except ZeroDivisionError:
            yield 4
            yield 5
            raise
        except:
            yield 6
            yield 7     # the "raise" above stops this
    except:
        yield 8
    yield 9
    try:
        x = 12
    finally:
        yield 10
    yield 11


for i in complicated_yield_generator():
    print(i)

# Until this, the coroutine f() cannot deliver values to the main routine.


# coroutine based on yield example
def yield_based_coroutine():
    print('callee 1')
    x = yield 1
    print('callee 2: %d' % x)
    x = yield 2            # main routine에서 가져온 값을 x에 삽입, 2를 main routine으로 전달
    print('callee 3: %d' % x)

task = yield_based_coroutine()
i = next(task)    # callee 1 출력, i는 1이 됨
i = task.send(10) # callee 2: 10 출력, i는 2가 됨
# next(task)
task.send(20)     # callee 3: 20 출력 후 StopIteration exception 발생

# Until this,
# The coroutine can deliver exception to the main routine, but not vice versa.
# but close() and throw() function appear in python2.5
# task = yield_based_coroutine()
# i = next(task)
# task.close()
