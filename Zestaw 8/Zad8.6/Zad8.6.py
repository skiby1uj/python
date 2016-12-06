from time import clock

P = {(0, 0): 0.5, (0, 1): 1.0, (1, 0): 0.0}

def DynamicFunction(i, j):
    if i < 0:
        raise ValueError("i jest mniejsze od 0")
    elif j < 0:
        raise ValueError("j jest mniejsze od 0")
    else:
        if i == 0:
            return 1.0
        elif j == 0:
            return 0.0
        else:
            tmp = P.get((i, j))
            if tmp != None:
                return tmp
            else:
                tmp = 0.5*(DynamicFunction(i-1, j)+DynamicFunction(i, j-1))
                P[(i, j)] = tmp
                return tmp

def RecursionFunction(i, j):
    if i < 0:
        raise ValueError("i jest mniejsze od 0")
    elif j < 0:
        raise ValueError("j jest mniejsze od 0")
    else:
        if i == 0 and j == 0:
            return 0.5
        elif i == 0:
            return 1.0
        elif j == 0:
            return 0.0
        else:
            return 0.5*(RecursionFunction(i-1, j)+RecursionFunction(i, j-1))

def test(i, j):
    startTime = clock()
    print "Recursion value: " +  str(RecursionFunction(i, j))
    time = clock() - startTime
    print "Time: " + str(time)
    startTime = clock()
    print "Dynamic value: " + str(DynamicFunction(i, j))
    time2 = clock() - startTime
    print "Time: " + str(time2)
    if time > time2:
        print 'Dynamic win'
    else:
        print 'Recursion win'
    print "-----------------------------------------"

test(0, 0)
test(3, 4)
test(3, 6)
test(0, 1)
test(7, 6)
test(12, 13)
test(20, 12)
