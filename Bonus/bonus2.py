from random import randint

random_number = randint(1, 10)
max_attempts = 3
for i in range(max_attempts):
    guess = int(input("Devinez le nombre entre 1 et 10 : "))
    if guess == random_number:
        print("Félicitations ! Vous avez deviné le nombre.")
        break
    elif guess < random_number:
        print("Trop bas ! Essayez encore.")
    else:
        print("Trop haut ! Essayez encore.")
    if i == max_attempts - 1:
        print(f"Désolé, vous avez épuisé vos tentatives. Le nombre était {random_number}.")