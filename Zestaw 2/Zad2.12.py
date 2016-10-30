#2.12
print('Zad 2.12\n');
line = "ab\tcd\nef\n";
line =  line.split();
print line;
firstCharsArray = [x[0] for x in line];
print "".join(x for x in firstCharsArray);

lastCharsArray = [x[-1] for x in line];
print "".join(x for x in lastCharsArray);