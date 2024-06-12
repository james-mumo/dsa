def fact(k):
    if k==0:
        return 1
    return k * fact(k-1)

print(fact(5))