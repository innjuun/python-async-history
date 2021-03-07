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
# Cannot deli
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

