def loopfib(n):
    prev = 1
    curr = 1
    for i in range(n-2):
        curr, prev = curr + prev, curr
        print("current value is", curr)

        print("previous value", prev)
    return curr

print(loopfib(5))


def recursionfib(n):
    if n < 3:
        return 1
    else:
        return recursionfib(n-1) + recursionfib(n-2)

print('recursion',recursionfib(5))
