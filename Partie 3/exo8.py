def tarif(age):
    if not isinstance(age, int):
        try:
            age = int(age)
        except:
            raise "Value Error"
    
    if age < 12:
        print("Enfant")
    elif (age >= 12) and (age <= 17):
        print("Adolescent")
    elif (age >= 18) and (age <= 64):
        print("Adulte")
    elif age >= 65:
        print("Senior")

tarif(6)
tarif(12)
tarif(17)
tarif(18)
tarif(64)
tarif(65)
tarif(69_420)

tarif("16")