import sys

i = 0


def ne():
    global i
    i += 1
    print("James", i)

    ne()


sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
ne()
