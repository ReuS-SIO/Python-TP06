
# Sujet du TP06 : Python – Les IF, ELSE, ELIF

```
TP0 6 : Python – Les IF, ELSE, ELIF
BLOC1 – BASE SLAM (orientée)
BTS SIO 1 - BLOC 1 - TP06 - Thème 2 : Python
LDU Dumbéa, Nouvelle-Calédonie
```
### TP0 6

# Thème 2 : Python

**Contexte :**

- Formation : BTS SIO (1ère année)
- Durée : 1 séances de 3 heures
- Objectif pédagogique **:** Initier les étudiants à l’environnement de programmation Python.

## SOMMAIRE :

I. PARTIE 1 : Tests simples .............................................................................................................. 3

1. Exercice 1 : le début ................................................................................................................... 3
2. Exercice 2 : Comparaison de nombres ....................................................................................... 3
3. Exercice 3 : Vérification d’un mot de passe .............................................................................. 3
II. PARTIE 2 : Utilisation des conditions ........................................................................................... 4
1. Exercice 4 : Calcul de moyenne ................................................................................................. 4
2. Exercice 5 : Pair ou impair ......................................................................................................... 4
3. Exercice 6 : Accès à une attraction ............................................................................................ 4
III. Partie 3 : fonctions avec condition ................................................................................................. 6
1. Exercice 7 : Fonction de majorité .............................................................................................. 6
2. Exercice 8 : Fonction de tarif ..................................................................................................... 6
3. Exercice 9 : Calculateur ............................................................................................................. 6
4. Exercice 10 : Vérification d’un identifiant ................................................................................ 7
IV. PARTIE BONUS : Pour ceux qui ont fini ..................................................................................... 8
1. Bonus 1 : Mot de passe avec 3 essais ........................................................................................ 8
2. Bonus 2 : Jeu du nombre mystère .............................................................................................. 8
3. Bonus 3 – Calcul de remise ....................................................................................................... 9
4. Bonus 4 : Validation de mot de passe ........................................................................................ 9


```
TP0 6 : Python – Les IF, ELSE, ELIF
BLOC1 – BASE SLAM (orientée)
BTS SIO 1 - BLOC 1 - TP06 - Thème 2 : Python
LDU Dumbéa, Nouvelle-Calédonie
```
## Python : l’entrée en matière

**Objectifs pédagogiques** :
o Être à l’aise avec les conditions en Python
**À la fin de la séance, l’étudiant doit pouvoir :**

- Utiliser if, elif, else
- Manipuler des booléens
- Utiliser des comparaisons
- Utiliser input()
- Écrire des fonctions avec conditions
- Comprendre paramètres et arguments


```
TP0 6 : Python – Les IF, ELSE, ELIF
BLOC1 – BASE SLAM (orientée)
BTS SIO 1 - BLOC 1 - TP06 - Thème 2 : Python
LDU Dumbéa, Nouvelle-Calédonie
ð Dans cette partie, je vous demande de ne pas créer des fonctions
ð Vous utiliserez print(), input()
```
# I. PARTIE 1 : Tests simples

## 1. Exercice 1 : le début

Créer un programme qui :

1. Demande l’âge de l’utilisateur
2. Affiche s’il est majeur ou mineur
Exemple :
Quel est votre âge? 19
Vous êtes majeur

## 2. Exercice 2 : Comparaison de nombres

Créer un programme qui :

1. Demande un nombre
2. Indique si ce nombre est :
- Positif
- Négatif
- Égal à zéro

## 3. Exercice 3 : Vérification d’un mot de passe

Créer un programme qui :

1. Demande un mot de passe
2. Compare avec "pYth0n123*%?"
Le programme doit afficher :
- Accès autorisé ou Accès refusé


```
TP0 6 : Python – Les IF, ELSE, ELIF
BLOC1 – BASE SLAM (orientée)
BTS SIO 1 - BLOC 1 - TP06 - Thème 2 : Python
LDU Dumbéa, Nouvelle-Calédonie
ð Dans cette partie, vous pouvez créer des fonctions ou non. Vous avez le choix.
```
# II. PARTIE 2 : Utilisation des conditions

## 1. Exercice 4 : Calcul de moyenne

Créer un programme qui :

1. Demande une note
2. Affiche :
    **condition message**
       note < 10 Ajourné
          10 à 12 Passable
          12 à 14 Assez Bien
          14 à 16 Bien
             16 et + Très bien

## 2. Exercice 5 : Pair ou impair

Créer un programme qui :

1. Demande un nombre entier
2. Indique s’il est pair ou impair
Indice :
Il vous faudra utiliser la fonction % (modulo) (allez voir sur Python.org !)

## 3. Exercice 6 : Accès à une attraction

Une attraction impose :

- Âge minimum : 12 ans
- Taille minimum : 140 cm


**TP0 6 : Python – Les IF, ELSE, ELIF
BLOC1 – BASE SLAM (orientée)**
BTS SIO 1 - BLOC 1 - TP06 - Thème 2 : Python
LDU Dumbéa, Nouvelle-Calédonie
Le programme doit demander :

- L’âge
- La taille
Puis afficher :
- Accès autorisé ou Accès refusé


```
TP0 6 : Python – Les IF, ELSE, ELIF
BLOC1 – BASE SLAM (orientée)
BTS SIO 1 - BLOC 1 - TP06 - Thème 2 : Python
LDU Dumbéa, Nouvelle-Calédonie
ð Dans cette partie, vous devez créer des fonctions.
```
# III. Partie 3 : fonctions avec condition

## 1. Exercice 7 : Fonction de majorité

Créer une fonction :
def verifier_majorite(age):
La fonction doit afficher :

- majeur
- mineur
Tester la fonction avec plusieurs âges.

## 2. Exercice 8 : Fonction de tarif

Créer une fonction :
def tarif(age):
Règles :
**âge tarif**
< 12 enfant
12 – 17 adolescent
18 – 64 adulte
65+ senior
Appeler la fonction avec plusieurs valeurs pour exemple.

## 3. Exercice 9 : Calculateur

Créer une fonction calculateur(nombre1, nombre2, opérateur) qui demande :

- Un premier nombre
- Un second nombre
- Une opération (+, -, *, /) indiquée en lettres : addition, soustraction, multiplication, division


**TP0 6 : Python – Les IF, ELSE, ELIF
BLOC1 – BASE SLAM (orientée)**
BTS SIO 1 - BLOC 1 - TP06 - Thème 2 : Python
LDU Dumbéa, Nouvelle-Calédonie
Puis afficher le résultat.

## 4. Exercice 10 : Vérification d’un identifiant

Créer une fonction connexion(login, mdp) qui demande :

- Un identifiant
- Un mot de passe
Conditions :
identifiant = "root"
mot_de_passe = "!!_Ca_C_pYthon_**"
Affichage :
- Connexion réussie ou Identifiant incorrect ou Mot de passe incorrect


```
TP0 6 : Python – Les IF, ELSE, ELIF
BLOC1 – BASE SLAM (orientée)
BTS SIO 1 - BLOC 1 - TP06 - Thème 2 : Python
LDU Dumbéa, Nouvelle-Calédonie
```
# IV. PARTIE BONUS : Pour ceux qui ont fini

/!\ Ces exercices peuvent introduire des notions non vues officiellement, comme les boucles.

## 1. Bonus 1 : Mot de passe avec 3 essais

Créer un programme qui :

- Demande un mot de passe
- Autorise 3 tentatives maximum
Si le mot de passe est correct :
Connexion réussie
Sinon :
Compte bloqué
Indice : while

## 2. Bonus 2 : Jeu du nombre mystère

Créer un programme :

- L’ordinateur choisit un nombre entre **1 et 10**
- L’utilisateur doit deviner
Le programme indique :
- Trop grand ou trop petit ou gagné
Indice : import random


```
TP0 6 : Python – Les IF, ELSE, ELIF
BLOC1 – BASE SLAM (orientée)
BTS SIO 1 - BLOC 1 - TP06 - Thème 2 : Python
LDU Dumbéa, Nouvelle-Calédonie
```
## 3. Bonus 3 – Calcul de remise

Créer une fonction :
def calcul_prix(prix):
Règles :
**prix réduction**
< 50 aucune
50 - 99 10 %
100 - 199 20 %
200+ 30 %
La fonction doit afficher le prix final, incluant la réduction appropriée.

## 4. Bonus 4 : Validation de mot de passe

Créer une fonction valide_mdp(mdp) qui vérifie si un mot de passe :

- Contient au moins 12 caractères
- Contient au moins un chiffre
- Contient au moins une majuscule
- Contient au moins un caractère spécial
Sinon afficher :
Mot de passe trop faible
Indice : len()


