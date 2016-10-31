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
