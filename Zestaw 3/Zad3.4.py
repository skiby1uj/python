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