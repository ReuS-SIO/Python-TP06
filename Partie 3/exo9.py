def calculateur(nombre1, nombre2, opérateur):
    eval_str = f"{nombre1} {opérateur} {nombre2}"
    print(eval(eval_str))

calculateur(390, 30, "+")  
calculateur(450, 30, "-")
calculateur(840, 2, "/") 
calculateur(210, 2, "*")