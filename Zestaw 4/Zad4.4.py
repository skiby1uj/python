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
