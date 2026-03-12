def valide_mdp(mdp):
    status = True
    if len(mdp) < 12:
        status = False
    x = "d"

    contient_chiffre = any(c.isdigit() for c in mdp)
    if not contient_chiffre:
        status = False

    contient_majuscule = any(c.isupper() for c in mdp)
    if not contient_majuscule:
        status = False
    
    contient_special = any(not c.isalnum() for c in mdp)
    if not contient_special:
        status = False
    
    if not status:
        print("Mot de passe trop faible.")
        return

    print("Mot de passe autorisé !")

valide_mdp("jdshf")
valide_mdp("Pdnsdsfqsdff")
valide_mdp("Jhdjkdsfq**dsf")
valide_mdp("Sdksfjkdsjf**6856")