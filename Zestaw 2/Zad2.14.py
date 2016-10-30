#2.14
print('Zad 2.14\n');
line = "ab\tcdqwd\nef\n";
line  = line.split();
print line;
print max([len(x) for x in line]);
print max(line, key=len);