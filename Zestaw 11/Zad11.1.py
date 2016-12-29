import random
import math

def randomNumberList(size):
    L = []
    for i in range(0, int((random.random())*1000)):
        L.append(random.randint(0, size-1))
    return L

def prawiePosortowana(size):
    L = []
    for i in range(0, int((random.random())*1000)):
        if i % 2 == 0:
            L.append(i+1)
        else:
            L.append(i-1)
    return L

def prawiePosortowanaOdwrotnie(size):
    L = prawiePosortowana(size)
    L.reverse()
    return L

def randomGauss(size, mu, sigma):
    L = []
    for x in range(0, int((random.random())*1000)):
        L.append(random.gauss(mu, sigma))
    return L

def randomNumberSet(size):
    L = []
    for i in range(0, size):
        L.append(random.randint(0, int(math.sqrt(size))))
    return L

# print randomNumberList(10)
# print prawiePosortowana(10)
# print prawiePosortowanaOdwrotnie(10)
# print randomGauss(1, 10, 1)
# print randomNumberSet(100)
