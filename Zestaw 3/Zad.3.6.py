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