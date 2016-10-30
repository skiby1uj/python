#2.10
print('Zad 2.10\n');
line = "ab\tcd\nef\n";
print line;
print len(line.split());

#2.11
print('Zad 2.11\n');
line = "qwerty";
print line;
tmp = line.replace('', '_');
tmp2 = tmp[1: -1];
print tmp2;

#2.12
print('Zad 2.12\n');
line = "ab\tcd\nef\n";
line =  line.split();
print line;
firstCharsArray = [x[0] for x in line];
print "".join(x for x in firstCharsArray);

lastCharsArray = [x[-1] for x in line];
print "".join(x for x in lastCharsArray);

#2.13
print('Zad 2.13\n');
line = "ab\tcd\nef\n";
line = line.split();
print line;
print sum([len(x) for x in line]);

#2.14
print('Zad 2.14\n');
line = "ab\tcdqwd\nef\n";
line  = line.split();
print line;
print max([len(x) for x in line]);
print max(line, key=len);

#2.15
print ('Zad 2.15\n');
L = [12, 11, 2];
print L;
print "".join(str(x) for x in L);

#2.16
print ('Zad 2.16\n');
line = 'What is GvR';
print line;
print line.replace('GvR', 'Guido van Rossum');

#2.17
print ('Zad 2.17\n');
line = "ab\tcdqwd\nef\n";
line = line.split();
print line;
line.sort();
print line;
line.sort(key = len);
print line;

#2.18
print('Zad 2.18\n');
bigInt = 6850080860856068007270700;
print bigInt;
string = str(bigInt);
print string.count('0');

#2.19
print('Zad 2.19\n');
L = [12, 1, 2, 3, 345, 3, 45, 243];
print L;
Lstr = [str(x).zfill(3) for x in L];
print ", ".join(x for x in Lstr);
