import numpy as np


def Support(Joueur,Probas):
    Indexes = []
    for i in range(len(Probas[Joueur - 1])):
        if Probas[Joueur - 1][i] != 0:
            Indexes.append(i) 
    return Indexes

def NotSupport(Joueur,Probas):
    Indexes = []
    for i in range(len(Probas[Joueur - 1])):
        if Probas[Joueur - 1][i] == 0:
            Indexes.append(i) 
    return Indexes

def Paiement(Joueur,Mat,Probas):
    returned = []
    if Joueur == 1:
        for i in range(len(Mat)):
            x = 0
            for j in range(len(Mat[0])):
                x += Mat[i][j][0] * Probas[1][j]
            returned.append(x)

    else:
        for j in range(len(Mat)):
            x = 0
            for i in range(len(Mat[0])):
                x += (Mat[i][j][1] * Probas[0][j])
            returned.append(x)
    return returned
                
def Utilite(Joueur,Mat,Probas):
    Inter = Paiement(Joueur,Mat,Probas)
    x = 0
    for i in range(len(Inter)):
        x += Inter[i] * Probas[Joueur - 1][i]
    return x

#It compares payments and utilities for both players.
def IndiSupp(Mat,Probas):
    Supp = Support(1,Probas), Support(2,Probas) 
    NotSupp = NotSupport(1,Probas), NotSupport(2,Probas) 

    for player in range(1,3):
        for i in range(len(Supp[player-1])):
            for j in range(i+1,len(Supp[player-1])):
                if(Paiement(player,Mat,Probas)[i]!=Paiement(player,Mat,Probas)[j] 
                   or Paiement(player,Mat,Probas)[i]>Utilite(player,Mat,Probas)):
                    return False

        for i in range(len(NotSupp[player-1])):
            for j in range(i+1,len(NotSupp[player-1])):
                if(Paiement(player,Mat,Probas)[i]!=Paiement(player,Mat,Probas)[j] 
                   or Paiement(player,Mat,Probas)[i]>Utilite(player,Mat,Probas)):
                    return False
                
    return True            
   

Mat = [[(4, 3), (5, 1), (6, 2)],
       [(2, 1), (8, 4), (3, 6)],
       [(3, 0), (9, 6), (2, 5)]]

Probas = [[1/3, 1/3, 1/3], [0, 1/2, 1/2]]


print("Support du joueur 1: ", Support(1,Probas), "\nSupport du joueur 2: ",Support(2,Probas),'\n')
print("Paiement du joueur 1: ", Paiement(1,Mat,Probas), "\nPaiement du joueur 2: ", Paiement(2,Mat,Probas),'\n')
print("Utilite du joueur 1: ", Utilite(1,Mat,Probas), "\nUtilite du joueur 2: ", Utilite(2,Mat,Probas),'\n')

if(IndiSupp(Mat,Probas)):
    print('Equilibre de Nash')
else:
    print('Pas d Equilibre de Nash')