#2.13
print('Zad 2.13\n');
line = "ab\tcd\nef\n";
line = line.split();
print line;
print sum([len(x) for x in line]);