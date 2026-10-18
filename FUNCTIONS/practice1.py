a = 4
b = 6
c = 9

average = a+b+c/3
print(average)

a1 = 4
b1 = 4
c1 = 0

average1 = a1+b1+c1/3
print(average1)


def getAverage(a,b,c):
    d = a+b+c/3
    print(d)

getAverage(4,6,7)
getAverage(4,6,8)


sum = lambda x : x+1
mul = lambda y:y*2
total = lambda x,y:x+y


print(sum(2))
print(mul(7))
print(total(8,3))