import math

def spr(a, b, c):
    tmp = [a, b, c]
    tmp.sort()
    if tmp[0] + tmp[1] >= tmp[-1]:
        return True
    return False

def heron(a, b, c):
    if(spr(a, b, c) == False):
        raise ValueError ("Warunek trojkata jest nie spelniony")
    polObw = (a + b + c)/2
    return math.sqrt(polObw * (polObw - a)*(polObw-b)*(polObw-c))



a = int(raw_input("Podaj a: "))
b = int(raw_input("Podaj b: "))
c = int(raw_input("Podaj c: "))
print heron(a, b, c)
