import random

class RandomQueue:

    def __init__(self, size=5):
        self.n = size+1       # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.end = -1           #ostatni element

    def is_full(self):
        return self.n <= self.end+1

    def insert(self, item):
        if self.is_full():
            raise ValueError("Kolejka jest pelna")
        self.items[self.end+1] = item
        self.end = self.end + 1

    def is_empty(self):
        return self.end < 0

    def remove(self):
        output = None
        if self.end == 0:
            output = self.items[0]
            self.items[0] = None
        elif self.is_empty():
            raise ValueError("Kolejka jest pusta")
        else:
            tmp = random.randint(0, self.end)
            # print "tmp = "+str(tmp)
            output = self.items[tmp]
            self.items[tmp] = self.items[self.end]
            self.items[self.end] = None
        self.end = self.end - 1
        return output

    def printQueue(self):
        i = 0
        while i <= self.end:
            print self.items[i]
            i = i + 1

    def count(self):
        return self.end+1
