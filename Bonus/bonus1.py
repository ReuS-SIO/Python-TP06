i = 0
max_attempts = 3
while i < max_attempts:
    mdp = input(f"Tentative restante {max_attempts - i}\nEntrez le mot de passe : ")
    if mdp == "pYth0n123*%?":
        print("Accès autorisé !")
        break
    else:
        print("Mot de passe incorrect\n\n")
        if i == max_attempts - 1:
            print("Nombre de tentatives maximum atteint. Compte bloqué.")
    i += 1