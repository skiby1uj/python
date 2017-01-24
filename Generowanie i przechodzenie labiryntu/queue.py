class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if (self.head + self.n-1) % self.n == self.tail:
            raise ValueError("Kolejka jest pelna!")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.head == self.tail:
            raise ValueError("Kolejka jest pusta")
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencje
        self.head = (self.head + 1) % self.n
        return data
