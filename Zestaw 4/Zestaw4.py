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

#Zad 4.3
print('Zad 4.3\n');
def factorial(n):
	if n == 0:
		return 1;
	output = 1;
	i = 1;
	while i <= n:
		output *= i
		i += 1
	return output;
n = int(raw_input("Z jakiej liczby silnia: "))
print factorial(n)

#Zad 4.4
print('Zad 4.4\n');
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	pierw = 0
	drug = 1
	output = 1
	i = 2;
	while(i <= n):
		output = pierw + drug;
		pierw = drug
		drug = output
		i += 1
	return output
n = int(raw_input("Ktora liczbe fibonacciego liczymy: "))
print fibonacci(n)

#Zad 4.5
print('Zad 4.5\n');
def odwracanieIter(L, left, right):
	while left < right:
		L[left], L[right] = L[right], L[left]
		left += 1
		right -= 1


lista  = [1, 2, 3, 4]
print lista
odwracanieIter(lista, 0, 3);
print lista

def odwracanieReq(L, left, right):
	if(left < right):
		L[left], L[right] = L[right], L[left]
		odwracanieReq(L, left+1, right - 1)

lista  = [1, 2, 3, 4]
print lista
odwracanieIter(lista, 1, 3);
print lista

#Zad 4.6
print('Zad 4.6\n');
def sum_seq(sequence):
	output = 0;
	if isinstance(sequence, (list, tuple)):
		for x in sequence:
			output += int(sum_seq(x))
	else:
		return sequence
	return output
sequence = [[],[4],(1,2),[3,4],(5,6,7)]
print sum_seq(sequence)


#Zad 4.7
print('Zad 4.7\n');
def flatten(sequence):
	output = list()
	if isinstance(sequence, (list, tuple)):
		for x in sequence:
			if isinstance(x, (list, tuple)):
				tmp = flatten(x)
				output += tmp
			else:
				output.append(x)
	return output

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print flatten(sequence)
