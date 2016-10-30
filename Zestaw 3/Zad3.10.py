#Zad3.10
print('Zad 3.10\n');
class roman2int:
	slownik = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	slownik2 = dict(IV=4, IX=9, XL=40, XC=90, CD=400)
	slownik2['CM'] = 900
	def convert(self, liczba):
		tab = [x for x in liczba]
		lenTab = len(tab)
		output = 0
		x = 0;
		while(x < lenTab):
			if(x < lenTab-1):
				tmp = str(tab[x]+tab[x+1])
				if(self.slownik2.has_key(tmp)):#liczba z slownik2
					output += self.slownik2[str(tab[x]+tab[x+1])]
					x += 1
				else:
					output += self.slownik[str(tab[x])]
			else:
				output += self.slownik[str(tab[x])]
			x += 1
		return output;


tmp = roman2int()
print tmp.convert('XXX')
print tmp.convert('IX')
print tmp.convert('XL')
print tmp.convert('CC')
print tmp.convert('CD')
print tmp.convert('CM')