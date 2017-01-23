import sys
from stack import Stack
from RandomQueue import RandomQueue

class Maze:
    def __init__(self, x):
        self.x = x
        self.value = [['#' for r in range(x)] for w in range(x)]

    # def __getitem__(self, x, y):
    #     return self.value[x][y]

    def checkNeigh(self, x, y):#sprawdza czy somsiedzi zostali odwiedzeni i zwraca jednego losowo
        randomQueue = RandomQueue()
        countShouldNeugh = None
        # print 'checkNeigh'
        if x > 0 and y > 0 and x < self.x-1 and y < self.x-1:
            countShouldNeugh = 4
            if str(self.value[x][y+1]) == '#':
                randomQueue.insert([x, y+1])
            if str(self.value[x][y-1]) == '#':
                randomQueue.insert([x, y-1])
            if str(self.value[x-1][y]) == '#':
                randomQueue.insert([x-1, y])
            if str(self.value[x+1][y]) == '#':
                randomQueue.insert([x+1, y])
        if x == 0 and y > 0 and y < self.x-1:
            countShouldNeugh = 3
            if str(self.value[x][y-1]) == '#':
                randomQueue.insert([x, y-1])
            if str(self.value[x][y+1]) == '#':
                randomQueue.insert([x, y+1])
            if str(self.value[x+1][y]) == '#':
                randomQueue.insert([x+1, y])
        if x > 0 and y == 0 and x < self.x-1:
            countShouldNeugh = 3
            if str(self.value[x-1][y]) == '#':
                randomQueue.insert([x-1, y])
            if str(self.value[x+1][y]) == '#':
                randomQueue.insert([x+1, y])
            if str(self.value[x][y+1]) == '#':
                randomQueue.insert([x, y+1])
        if x > 0 and y == self.x-1 and x < self.x-1:
            countShouldNeugh = 3
            if str(self.value[x+1][self.x-1]) == '#':
                randomQueue.insert([x+1, self.x-1])
            if str(self.value[x-1][self.x-1]) == "#":
                randomQueue.insert([x-1, self.x-1])
            if str(self.value[x][y-1]) == "#":
                randomQueue.insert([x, y-1])
        if x == self.x-1 and y > 0 and y < self.x-1:
            countShouldNeugh = 3
            if str(self.value[self.x-1][y+1]) == "#":
                randomQueue.insert([self.x-1, y+1])
            if str(self.value[(self.x)-1][y-1]) == '#':
                randomQueue.insert([(self.x)-1, y-1])
            if str(self.value[x-1][y]) == '#':
                randomQueue.insert([x-1, y])
        if x == 0 and y == 0:
            countShouldNeugh = 2
            if str(self.value[x+1][y]) == '#':
                randomQueue.insert([x+1, y])
            if str(self.value[x][y+1]) == '#':
                randomQueue.insert([x, y+1])
        if x == 0 and y == self.x-1:
            countShouldNeugh = 2
            if str(self.value[x][y-1]) == '#':
                randomQueue.insert([x, y-1])
            if str(self.value[x+1][y]) == '#':
                randomQueue.insert([x+1, y])
        if x == self.x-1 and y == 0:
            countShouldNeugh = 2
            if str(self.value[x][y+1]) == '#':
                randomQueue.insert([x, y+1])
            if str(self.value[x-1][y]) == '#':
                randomQueue.insert([x-1, y])
        if x == self.x-1 and y == self.x-1:
            countShouldNeugh = 2
            if str(self.value[x][y-1]) == '#':
                randomQueue.insert([x, y-1])
            if str(self.value[x-1][y]) == '#':
                randomQueue.insert([x-1, y])
        if randomQueue.is_empty() == True:
            # print'randomQueue jest puste'
            return None, None, None
        # print 'koniec'
        # randomQueue.printQueue()
        return randomQueue.count(), randomQueue, countShouldNeugh

    def printLab(self):
        for i in range(0,self.x+2):
            sys.stdout.write('*')
        print
        for i in range(0, self.x):
            sys.stdout.write('*')
            for j in range(0, self.x):
                sys.stdout.write(self.value[i][j])
            print '*'
        for i in range(0,self.x+2):
            sys.stdout.write('*')
        print

    def generate(self):
        # print "in generate:"
        odl = 0
        sett = RandomQueue((self.x)*(self.x))
        stack = Stack((self.x)*(self.x))
        count, params, countShouldNeigh = self.checkNeigh(0,0)
        self.value[0][0] = 'S'
        stack.push(params)

        while not stack.is_empty():
            # stack.printStack()
            pop = stack.pop()
            randomNeighParam = pop.remove()#x, y sasiada do ktorego ide
            if not pop.is_empty():#jesli cos jest jeszcze w naszym random to odkladamy na stos
                stack.push(pop)
            # print 'Pole w ktorym jestem - ' + str(randomNeighParam) + " count: " + str(count) + " should: " + str(countShouldNeigh) + " do ktorego chce isc: " + str(param)
            count, params, countShouldNeigh = self.checkNeigh(randomNeighParam[0],randomNeighParam[1])
            if params is not None and count+1 == countShouldNeigh:
                stack.push(params)
                self.value[randomNeighParam[0]][randomNeighParam[1]] = ' '
                odl += 1#odl od poczatku lab
                if odl > self.x-1:
                    sett.insert(randomNeighParam)#dodajemy do randomQueue
            else:
                odl -= 1
        # self.printLab()
        tmp = sett.remove()
        self.value[tmp[0]][tmp[1]] = 'M'
        # print str(tmp)

tmp = Maze(10)
# tmp.printLab()
tmp.generate()
tmp.printLab()
