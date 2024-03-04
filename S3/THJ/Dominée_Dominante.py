import numpy as np

Strats = np.array([
                    [(3, 2), (7, 4), (4, 0)],
                    [(2, 1), (1, 3), (2, 1)],
                    [(4, 2), (8, 4), (5, 0)],
                    [(1, 4), (0, 5), (0, 2)]])

Strats2 = np.array([[(4, 3), (5, 1), (6, 2)],
                    [(2, 1), (8, 4), (3, 6)],
                    [(3, 0), (9, 6), (2, 8)]])


def StratDominante(Strats, joueur):
    BestStrat = -1
    strat_temp = -1

    if joueur == 1 :
        #pour le joueur 1 on parcour les colones
        for stratJ2_indx in range(len(Strats[0])):
            BestStratJ1 = -float("inf")
            for stratJ1_indx in range (len(Strats)):
                if BestStratJ1 < Strats[stratJ1_indx, stratJ2_indx, 0]:
                    BestStratJ1 = Strats[stratJ1_indx, stratJ2_indx, 0]
                    strat_temp = stratJ1_indx
                
            if BestStrat == -1 : 
                BestStrat = strat_temp
            elif BestStrat != strat_temp : 
                return "il n'a pas de strategie dominante"
        return BestStrat
    
    elif joueur == 2:
        # pour le joueur 2 on parcour les lignes
        for stratJ1_indx in range(len(Strats)):
            BestStratJ2 = -float("inf")
            for stratJ2_indx in range (len(Strats[0])):
                if BestStratJ2 < Strats[stratJ1_indx, stratJ2_indx, 1]:
                    BestStratJ2 = Strats[stratJ1_indx, stratJ2_indx, 1]
                    strat_temp = stratJ2_indx
                
            if BestStrat == -1 : 
                BestStrat = strat_temp
            elif BestStrat != strat_temp : 
                return "il n'a pas de strategie dominante"
        return BestStrat

def StratDomineeJ1(Strats):
    Result = Strats
    Strat = -1
    StratJ1_line1 = 0
    br = False

    while(StratJ1_line1 < len(Result)-1):
        StratJ1_line2 = StratJ1_line1+1
        while(StratJ1_line2 < len(Result)):
            strat = -1
            strat_temp = -1
            br = False
            StratJ2 = 0
            while(StratJ2 < len(Result[0])):
                if (Result[StratJ1_line1, StratJ2, 0] < Result[StratJ1_line2, StratJ2, 0]):
                    strat_temp = StratJ1_line1
                elif (Result[StratJ1_line1, StratJ2, 0] > Result[StratJ1_line2, StratJ2, 0]):
                    strat_temp = StratJ1_line2
                
                StratJ2+=1
                if strat == -1:
                    strat = strat_temp
                elif strat != strat_temp:
                    br = True
                    break
            if strat == -1 :
                br = True
            if br == False :
                Result = np.delete(Result, strat, 0)
            StratJ1_line2 += 1

        if br == True :
            StratJ1_line1+=1
    return Result

def StratDomineeJ2(Strats):
    Result = Strats
    Strat = -1
    StratJ2_col1 = 0
    br = False

    while(StratJ2_col1 < len(Result[0])-1):
        StratJ2_col2 = StratJ2_col1+1
        while(StratJ2_col2 < len(Result[0])):
            strat = -1
            strat_temp = -1
            br = False
            StratJ1 = 0
            while(StratJ1 < len(Result)):
                if (Result[StratJ1, StratJ2_col1, 1] < Result[StratJ1, StratJ2_col2, 1]):
                    strat_temp = StratJ2_col1
                elif (Result[StratJ1, StratJ2_col1, 1] > Result[StratJ1, StratJ2_col2, 1]):
                    strat_temp = StratJ2_col2
                
                StratJ1+=1
                if strat == -1:
                    strat = strat_temp
                elif strat != strat_temp:
                    br = True
                    break
            if strat == -1 :
                br = True
            if br == False :
                Result = np.delete(Result, strat, 1)

            StratJ2_col2 += 1
        if br == True :
            StratJ2_col1+=1
    return Result

def StratDominee(Strats):
    condition = True
    while condition:
        resultat_line = StratDomineeJ1(Strats)
        resultat_colone = StratDomineeJ2(resultat_line)
        if np.shape(resultat_line) == np.shape(resultat_colone):
            condition = False
            break
        else : Strats = resultat_colone
    return resultat_colone

print(StratDominante(Strats, 1))
print(StratDominee(Strats2))







