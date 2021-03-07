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
# task.send(20)     # callee 3: 20 출력 후 StopIteration exception 발생

# Until this,
# The coroutine can deliver exception to the main routine, but not vice versa.
# but close() and throw() function appear in python2.5
# task = yield_based_coroutine()
# i = next(task)
# task.close()


def coro():
    a = yield 1
    print('after first yield, a = {}'.format(a))
    yield a
    print('finish coro')

c = coro()
value = next(c)
print('first yield =',value)
print('last yield =',c.send(value + 1))
