
#1 grille du jeu 3*3

#def grille(tab):
   # for i in range(3):
      # for j in range(3):
         #  print(tab, end=" ")
#grille("0")

def grille(case):
    tab = [0,0,0,0,0,0,0,0,0]
    print(tab[0], tab[1], tab[2])
    print(tab[3], tab[4], tab[5])
    print(tab[6], tab[7], tab[8])


#2 jouer O ou X
def jouer(tab):    
    print("joueur 1 = X")
    choix1 = int(input("choisissez une case\n"))
    tab[choix1] = "X"
 
    print("joueur 2 = X")
    choix2 = int(input("choisissez une case\n"))
    tab[choix2] = "X"


#3 verification alignement de 3 symboles : verticale, horizontale, diagonale
def verif(tab):
   #verif horizontale :
   for i in range(len(tab)):
        if tab[i] == tab[i +1] == tab[i +2]:
            
    return

#4 verification de la grille complete
def complete(case, tab):
    remplie = True
    while(remplie):
        remplie = False
        for i in range(len(tab)):
            if tab[i] == "X" or "O":
                remplie = True
            else:
                remplie = False
                print("la grille n'est pas complete ")
    return

#5 jouer à 2

grille(0)

complete() = True 
verif = True
while(complete):
    complete = False
    jouer
    print(grille)
    if verif == False :
        complete() = False
    else:   
        complete() = True
    
#6 Qu’aura-t-on besoin de faire, si on souhaite désormais programmer un jeu de
#  Puissance 4 ?

# Il y aurait besoin de modifier la vérification de l'alignement en passant de 3 symboles a 4.
# Mais il faudrait aussi modifier la grille en l'agrandissant.
# Et on ne peut que choisir de jouer sur les colonnes et si les cases ne sont pas deja joué le symbole est placé sur la ligne la plus basse posssible.