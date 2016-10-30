#Zad 4.7
print('Zad 4.7\n');
def flatten(sequence):
	output = list()
	if isinstance(sequence, (list, tuple)):
		lenSeq = len(sequence)
		for x in range(lenSeq):
			if isinstance(sequence[x], (list, tuple)):
				tmp = flatten(sequence[x])
				output += tmp
			else:
				output.append(sequence[x])
	return output

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print flatten(sequence)
