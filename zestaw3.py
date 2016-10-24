#Zad3.3
print('Zad 3.3\n');
for x in range(30):
    if x % 3 != 0:
        print x

#Zad3.4
print('Zad 3.4\n');
while True:
	try:
		line = (raw_input("Podaj liczbe: "))
		n = int(line)
		print str(n) + ' ' + str(pow(n, 3))
		
	except ValueError:
		if(line == 'stop'):
			break;
		print 'Nie podales liczby! Sprobuj jeszcze raz'

#Zad3.5
print('Zad 3.5\n');
n = int(raw_input("Podaj dlugosc miarki: "))
output = '|'
for x in range(n):
	output += '....|'
	x = x +1;
output += '\n0';
for x in range(n):
	nextIntX = x + 1;
	x = str(nextIntX);
	nextLenX = len(x);
	while (5 - nextLenX):
		output += ' ';
		nextLenX += 1;
	output += x;
print output;

#Zad3.6
print('Zad 3.6\n');
x = int(raw_input("Podaj wartosc x: "));
y = int(raw_input("Podaj wartosc y: "));

def liniaZeSpacjami(dlugosc):
	output = '|'
	for x in range(dlugosc):
		output += '   |';
	return output + '\n';

def liniaZplusami(dlugosc):
	output = '+';
	for x in range(dlugosc):
		output += '---+';
	return output + '\n';

def rysujKratke(dlugosc, wysokosc):
	output = '';
	for x in range(wysokosc):
		output += liniaZplusami(dlugosc);
		output += liniaZeSpacjami(dlugosc);
	output += liniaZplusami(dlugosc);
	return output;

output = rysujKratke(x, y);
print output;

#Zad3.8
print('Zad 3.8\n');
t = [1,2,3,4]
print t
e = ['a', 'b','c', 1]
print e
lista = list(set(e + t))
print lista
lista = list(set(t).intersection(set(e)))
print lista

#Zad3.9
print('Zad 3.9\n');
sek1 = [[],[4],(1,2),[3,4],(5,6,7)]
print sek1;
print [sum(x) for x in sek1]


#Zad3.10
print('Zad 3.10\n');
class roman2int:
	slownik = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	slownik2 = dict(IV=4, IX=9, XL=40, XC=90, CD=400)
	slownik2['CM'] = 900
	def convert(self, liczba):
		tab = [x for x in liczba]
		lenTab = len(tab)
		output = 0
		x = 0;
		while(x < lenTab):
			if(x < lenTab-1):
				tmp = str(tab[x]+tab[x+1])
				if(self.slownik2.has_key(tmp)):#liczba z slownik2
					output += self.slownik2[str(tab[x]+tab[x+1])]
					x += 1
				else:
					output += self.slownik[str(tab[x])]
			else:
				output += self.slownik[str(tab[x])]
			x += 1
		return output;


tmp = roman2int()
print tmp.convert('XXX')
print tmp.convert('IX')
print tmp.convert('XL')
print tmp.convert('CC')
print tmp.convert('CD')
print tmp.convert('CM')