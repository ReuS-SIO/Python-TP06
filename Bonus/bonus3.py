def calcul_prix(prix):
    if prix < 50:
        return prix
    elif 50 <= prix < 100:
        return prix * 0.9
    elif 100 <= prix < 200:
        return prix * 0.8
    elif prix >= 200:
        return prix * 0.7

print(calcul_prix(49))
print(calcul_prix(55))
print(calcul_prix(100))
print(calcul_prix(201))