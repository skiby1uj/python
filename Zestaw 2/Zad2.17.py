#2.17
print ('Zad 2.17\n');
line = "ab\tcdqwd\nef\n";
line = line.split();
print line;
line.sort();
print line;
line.sort(key = len);
print line;