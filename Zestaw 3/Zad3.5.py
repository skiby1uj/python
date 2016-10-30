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