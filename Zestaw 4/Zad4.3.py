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
