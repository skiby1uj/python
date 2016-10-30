#2.19
print('Zad 2.19\n');
L = [12, 1, 2, 3, 345, 3, 45, 243];
print L;
Lstr = [str(x).zfill(3) for x in L];
print ", ".join(x for x in Lstr);
