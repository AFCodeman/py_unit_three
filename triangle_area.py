import math


def area(a,b,c):
    s=(a+b+c)/2
    A= (s*(s-a)*(s-b)*(s-c))**0.5
    return A

print(area(1,3,9))

