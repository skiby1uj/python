import sys
from stack import Stack
from RandomQueue import RandomQueue

class Maze:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = [['#' for r in range(x)] for w in range(y)]

    # def __getitem__(self, x, y):
    #     return self.value[x][y]

    def checkNeigh(self, x, y):#sprawdza czy somsiedzi zostali odwiedzeni i zwraca jednego losowo
        randomQueue = RandomQueue()
        countShouldNeugh = None
        # print 'checkNeigh'
        if x > 0 and y > 0 and x < self.x-1 and y < self.y-1:
            countShouldNeugh = 4
            if str(self.value[x][y+1]) == '#':
                randomQueue.insert([x, y+1])
            if str(self.value[x][y-1]) == '#':
                randomQueue.insert([x, y-1])
            if str(self.value[x-1][y]) == '#':
                randomQueue.insert([x-1, y])
            if str(self.value[x+1][y]) == '#':
                randomQueue.insert([x+1, y])
        if x == 0 and y > 0 and y < self.y-1:
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
        if x > 0 and y == self.y-1 and x < self.x-1:
            countShouldNeugh = 3
            if str(self.value[x+1][self.y-1]) == '#':
                randomQueue.insert([x+1, self.y-1])
            if str(self.value[x-1][self.y-1]) == "#":
                randomQueue.insert([x-1, self.y-1])
            if str(self.value[x][y-1]) == "#":
                randomQueue.insert([x, y-1])
        if x == self.x-1 and y > 0 and y < self.y-1:
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
        if x == 0 and y == self.y-1:
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
        if x == self.x-1 and y == self.y-1:
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
        return randomQueue.count(), randomQueue.remove(), countShouldNeugh

    def printLab(self):
        for i in range(0, self.x):
            for j in range(0, self.y):
                sys.stdout.write(self.value[i][j])
            print

    def generate(self):
        # print "in generate:"
        stack = Stack((self.x)*(self.y))
        # count, param, countShouldNeigh = self.checkNeigh(0,0)
        # print 'Ile jest: ' + str(count)
        # print 'Param: ' + str(param)
        # print 'Count Should: ' + str(countShouldNeigh)
        param = [0,0]
        count = None
        countShouldNeigh = None
        self.value[0][0] = '-'
        stack.push([0, 0])

        while not stack.is_empty():
            # stack.printStack()
            pop = stack.pop()
            count, param, countShouldNeigh = self.checkNeigh(pop[0], pop[1])#spr somsiada
            if param is not None:
                if count is not None and count > 1:
                    stack.push(pop)
                print 'Pole w ktorym jestem - ' + str(pop) + " count: " + str(count) + " should: " + str(countShouldNeigh) + " do ktorego chce isc: " + str(param)

                count, nextParam, countShouldNeigh = self.checkNeigh(param[0], param[1])#spr somsiada
                if nextParam is not None and count+1 == countShouldNeigh:
                    stack.push(param)
                    self.value[param[0]][param[1]] = '-'
                elif self.value[param[0]][param[1]] == '#':
                    self.value[param[0]][param[1]] = 'x'




tmp = Maze(3,3)
tmp.printLab()
tmp.generate()
tmp.printLab()
