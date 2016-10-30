#Zad 4.5
print('Zad 4.5\n');
def odwracanieIter(L, left, right):
	while left < right:
		L[left], L[right] = L[right], L[left]
		left += 1
		right -= 1


lista  = [1, 2, 3, 4]
print lista
odwracanieIter(lista, 0, 3);
print lista

def odwracanieReq(L, left, right):
	if(left < right):
		L[left], L[right] = L[right], L[left]
		odwracanieReq(L, left+1, right - 1)

lista  = [1, 2, 3, 4]
print lista
odwracanieIter(lista, 1, 3);
print lista
