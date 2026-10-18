def getRecursion(a):

    if a<=1:
        return 1
    else:
        return a * getRecursion(a-1)




res = getRecursion(3)
print(res)


