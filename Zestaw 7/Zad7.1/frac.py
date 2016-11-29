class Frac:
    """Klasa reprezentujaca ulamki."""

    def __init__(self, x=0, y=1):
        if isinstance(x, int) == False and isinstance(x, float) == False:
            raise ValueError("x nie jest typu numerycznego")
        if isinstance(y, int) == False and isinstance(y, float) == False:
            raise ValueError("y nie jest typu numerycznego")
        if y == 0:
            raise ValueError ("Mianownik ulamka nie moze byc 0")

        # Sprawdzamy, czy y=0.
        self.x = x
        self.y = y

    def __str__(self):       # zwraca "x/y" lub "x" dla y=1
    	if self.y == 1:
            return str(self.x)
        return str(self.x)+'/'+str(self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
		return str("Frac(" + str(self.x) + ","+str(self.y) + ")")


    def __cmp__(self, other):  # porownywanie
    	tmp1 = float(self)
        tmp2 = float(other)
        if tmp1 == tmp2:
            return 0
        elif tmp1 > tmp2:
            return 1
        return -1

    def __add__(self, other):  # frac1+frac2, frac+int
        if isinstance(other, int):
            return Frac(self.x + (self.y * other), self.y)
    	if self.y == other.y:
            return Frac(self.x + other.x, self.y)
        return Frac((self.x * other.y) + (other.x * self.y) , self.y * other.y)

    __radd__ = __add__              # int+frac

    def __sub__(self, other):  # frac1-frac2, frac-int
        if isinstance(other, int):
            return Frac(self.x - (self.y * other), self.y)
        if self.y == other.y:
            return Frac(self.x - other.x, self.y)
        return Frac((self.x * other.y) - (other.x * self.y) , self.y * other.y)

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):  # frac1*frac2, frac*int
        if isinstance(other, int):
            return Frac(self.x * other, self.y)
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__              # int*frac

    def __div__(self, other):  # frac1/frac2, frac/int
        if other == 0:
            raise ValueError ("Nie mozna dzielic przez 0")
        if isinstance(other, int):
            return Frac(self.x, self.y* other)
        return Frac(self.x * other.y, self.y * other.x);

    def __rdiv__(self, other): # int/frac
        if self == 0:
            raise ValueError ("Nie mozna dzielic przez 0")
        return Frac(self.y * other, self.x)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):         # -frac = (-1)*frac
    	return Frac(-self.x, self.y)

    def __invert__(self):      # odwrotnosc: ~frac
    	return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
    	return float(self.x)/float(self.y)
