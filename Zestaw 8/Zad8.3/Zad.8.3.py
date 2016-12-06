import random
import math

#pi = 4Pkola/Pkwad

def estimatePi(iloscTestow):
    i = poleKola = poleKw = 0
    r = 1
    while i < iloscTestow:
        i += 1
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        odl = odlOdSrodka(x, y)
        if odl <= r:
            poleKola += 1
        else:
            poleKw += 1
    if poleKw == 0:
        raise ValueError ("Dzielenie przez 0")
    return poleKola / float(poleKw)

def odlOdSrodka(x, y):
    return math.sqrt(math.pow(x, 2) + pow(y, 2))

iloscTestow = int(raw_input("Podaj ilosc losowanych punktow do przyblizenia\n(im wieksza tym lepsza dokladnosc): "));

print estimatePi(iloscTestow)
