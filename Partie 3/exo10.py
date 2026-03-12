def connexion(login, mdp):
    if login == "root":
        if mdp == "!!_Ca_C_pYthon_**":
            print("Accès autorisé !")
        else:
            print("Mot de passe incorrect")
    else:
        print("Identifiant incorrect")

connexion("Yoyo", "azerty")
connexion("root", "azerty")
connexion("root", "!!_Ca_C_pYthon_**")