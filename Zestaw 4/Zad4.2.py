#Zad 4.2
print('Zad 4.2 (3.5)\n');
n = int(raw_input("Podaj dlugosc miarki: "))
def miarka(dlugosc):
	output = '|'
	for x in range(dlugosc):
		output += '....|'
		x = x +1;
	output += '\n0';
	for x in range(dlugosc):
		nextIntX = x + 1;
		x = str(nextIntX);
		nextLenX = len(x);
		while (5 - nextLenX):
			output += ' ';
			nextLenX += 1;
		output += x;
	return output;
print miarka(n);


print('Zad 4.2 (3.6)\n');
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
print rysujKratke(x, y);
