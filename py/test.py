def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-2)+fib(i-1)

for x in range(10):
    print(fib(x))