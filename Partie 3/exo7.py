def verifier_majorite(age):
    if int(age) >= 18:
        print("Vous êtes majeur.")
        return 
    print("Vous êtes mineur.")

verifier_majorite(32)
verifier_majorite(6)
verifier_majorite(14)
verifier_majorite(99)
# Bonus:
verifier_majorite("16")
