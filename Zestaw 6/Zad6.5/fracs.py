class Frac:

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        return str(self.x)+'/'+str(self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return str("Frac(" + str(self.x) + ","+str(self.y) + ")")
        # return Frac(self.x, self.y)

    def __add__(self, other):
        if self.y == other.y:
            return Frac(self.x + other.x, self.y)
        return Frac((self.x * other.y) + (other.x * self.y) , self.y * other.y)

    def __sub__(self, other):
        if self.y == other.y:
            return Frac(self.x - other.x, self.y)
        return Frac((self.x * other.y) - (other.x * self.y) , self.y * other.y)

    def __mul__(self, other):  # frac1 * frac2
        return Frac(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return Frac(self.x * other.y, self.y * other.x);

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __cmp__(self, other):  # cmp(frac1, frac2)
        tmp1 = float(self)
        tmp2 = float(other)
        if tmp1 == tmp2:
            return 0
        elif tmp1 > tmp2:
            return 1
        return -1

    def __float__(self):       # float(frac)
        return float(self.x)/float(self.y)