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
