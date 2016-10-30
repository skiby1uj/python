#Zad3.8
print('Zad 3.8\n');
t = [1,2,3,4]
print t
e = ['a', 'b','c', 1]
print e
lista = list(set(e + t))
print lista
lista = list(set(t).intersection(set(e)))
print lista