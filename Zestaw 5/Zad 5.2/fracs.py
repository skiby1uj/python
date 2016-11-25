def add_frac(frac1, frac2):
	if frac1[1] == frac2[1]:
		return [frac1[0] + frac2[0], frac1[1]]
	return [(frac1[0] * frac2[1]) + (frac2[0] * frac1[1]) , frac1[1] * frac2[1]]

def sub_frac(frac1, frac2):
	if frac1[1] == frac2[1]:
		return [frac1[0] - frac2[0], frac1[1]]
	return [(frac1[0] * frac2[1]) - (frac2[0] * frac1[1]) , frac1[1] * frac2[1]]

def mul_frac(frac1, frac2):
	return [frac1[0] * frac2[0], frac1[1] * frac2[1]]

def div_frac(frac1, frac2):
	return [(frac1[0] * frac2[1]), (frac1[1] * frac2[0])]

def is_positive(frac):
	if frac2float(frac) > 0:
		return True
	return False

def is_zero(frac):
	if frac[0] == 0:
		return True
	return False

def frac2float(frac):
	frac[0] = float(frac[0])
	frac[1] = float(frac[1])
	return (frac[0] / frac[1])
	
def cmp_frac(frac1, frac2):
	tmp1 = frac2float(frac1)
	tmp2 = frac2float(frac2)
	if tmp1 == tmp2:
		return 0
	elif tmp1 > tmp2:
		return 1
	return -1
