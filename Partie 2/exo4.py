note = int(input("Entrez votre note: "))

if note < 10:
    print("Ajourné")
elif note >= 10 and note < 12:
    print("Passable")
elif note >= 12 and note < 14:
    print("Assez bien")
elif note >= 14 and note < 16:
    print("Bien")
elif note >= 16:
    print("Très bien")
