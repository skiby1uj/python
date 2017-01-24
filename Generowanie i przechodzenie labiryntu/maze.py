import sys
from stack import Stack
from RandomQueue import RandomQueue
from queue import Queue

class Maze:
    def __init__(self, x):
        self.x = x
        self.value = [['#' for r in range(x)] for w in range(x)]
        self.parent = [[[] for r in range(x)] for w in range(x)]

    # def __getitem__(self, x, y):
    #     return self.value[x][y]

    def checkNeigh(self, x, y, maze):#sprawdza czy somsiedzi zostali odwiedzeni i zwraca jednego losowo
        randomQueue = RandomQueue()
        countShouldNeugh = None
        # print 'checkNeigh'
        if x > 0 and y > 0 and x < self.x-1 and y < self.x-1:
            countShouldNeugh = 4
            if str(maze[x][y+1]) == '#':
                randomQueue.insert([x, y+1])
            if str(maze[x][y-1]) == '#':
                randomQueue.insert([x, y-1])
            if str(maze[x-1][y]) == '#':
                randomQueue.insert([x-1, y])
            if str(maze[x+1][y]) == '#':
                randomQueue.insert([x+1, y])
        if x == 0 and y > 0 and y < self.x-1:
            countShouldNeugh = 3
            if str(maze[x][y-1]) == '#':
                randomQueue.insert([x, y-1])
            if str(maze[x][y+1]) == '#':
                randomQueue.insert([x, y+1])
            if str(maze[x+1][y]) == '#':
                randomQueue.insert([x+1, y])
        if x > 0 and y == 0 and x < self.x-1:
            countShouldNeugh = 3
            if str(maze[x-1][y]) == '#':
                randomQueue.insert([x-1, y])
            if str(maze[x+1][y]) == '#':
                randomQueue.insert([x+1, y])
            if str(maze[x][y+1]) == '#':
                randomQueue.insert([x, y+1])
        if x > 0 and y == self.x-1 and x < self.x-1:
            countShouldNeugh = 3
            if str(maze[x+1][self.x-1]) == '#':
                randomQueue.insert([x+1, self.x-1])
            if str(maze[x-1][self.x-1]) == "#":
                randomQueue.insert([x-1, self.x-1])
            if str(maze[x][y-1]) == "#":
                randomQueue.insert([x, y-1])
        if x == self.x-1 and y > 0 and y < self.x-1:
            countShouldNeugh = 3
            if str(maze[self.x-1][y+1]) == "#":
                randomQueue.insert([self.x-1, y+1])
            if str(maze[(self.x)-1][y-1]) == '#':
                randomQueue.insert([(self.x)-1, y-1])
            if str(maze[x-1][y]) == '#':
                randomQueue.insert([x-1, y])
        if x == 0 and y == 0:
            countShouldNeugh = 2
            if str(maze[x+1][y]) == '#':
                randomQueue.insert([x+1, y])
            if str(maze[x][y+1]) == '#':
                randomQueue.insert([x, y+1])
        if x == 0 and y == self.x-1:
            countShouldNeugh = 2
            if str(maze[x][y-1]) == '#':
                randomQueue.insert([x, y-1])
            if str(maze[x+1][y]) == '#':
                randomQueue.insert([x+1, y])
        if x == self.x-1 and y == 0:
            countShouldNeugh = 2
            if str(maze[x][y+1]) == '#':
                randomQueue.insert([x, y+1])
            if str(maze[x-1][y]) == '#':
                randomQueue.insert([x-1, y])
        if x == self.x-1 and y == self.x-1:
            countShouldNeugh = 2
            if str(maze[x][y-1]) == '#':
                randomQueue.insert([x, y-1])
            if str(maze[x-1][y]) == '#':
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
        count, params, countShouldNeigh = self.checkNeigh(0,0, self.value)
        self.value[0][0] = 'S'
        stack.push(params)

        while not stack.is_empty():
            # stack.printStack()
            pop = stack.pop()
            randomNeighParam = pop.remove()#x, y sasiada do ktorego ide
            if not pop.is_empty():#jesli cos jest jeszcze w naszym random to odkladamy na stos
                stack.push(pop)
            # print 'Pole w ktorym jestem - ' + str(randomNeighParam) + " count: " + str(count) + " should: " + str(countShouldNeigh) + " do ktorego chce isc: " + str(param)
            count, params, countShouldNeigh = self.checkNeigh(randomNeighParam[0],randomNeighParam[1], self.value)
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
    def goingThroughMaze(self):
        checked = [['#' for r in range(self.x)] for w in range(self.x)]
        queue = Queue(self.x * self.x)
        queue.put([0,0])
        while not queue.is_empty():
            q = queue.get()
            if self.value[q[0]][q[1]] == 'M':#jesli meta to return
                return q
            tmp, neighs, tmp2 = self.checkNeigh(q[0], q[1], checked)
            while neighs is not None and not neighs.is_empty():
                tmp = neighs.remove()
                checked[tmp[0]][tmp[1]] = ' '
                self.parent[tmp[0]][tmp[1]] = q
                queue.put(tmp)

    def drawExitWay(self, exitPoint):
        while not(exitPoint[0] == 0 and exitPoint[1] == 0):

            # print str(exitPoint[0])
            # print str(exitPoint[1])
            pointParent = self.parent[exitPoint[0]][exitPoint[1]]
            self.value[pointParent[0]][pointParent[1]] = 'z'
            exitPoint = pointParent
        self.value[0][0] = 'S'



tmp = Maze(10)
# tmp.printLab()
tmp.generate()
tmp.printLab()
exitPoint = tmp.goingThroughMaze()
print exitPoint
tmp.drawExitWay(exitPoint)
tmp.printLab()
