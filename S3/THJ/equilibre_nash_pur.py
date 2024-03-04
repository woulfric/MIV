import numpy as np


matrix = np.array([
    [[2, 1], [0, 0]],
    [[0,0], [1, 2]]
])

indice1 = []
for i in range(len(matrix)):

    indice = np.argmax(matrix[i][:, 0])
    indice1.append([i, indice])

indices2 = []
for j in range(matrix.shape[2]):

    indice2 = np.argmax(matrix[:, :, 1][:, j])
    indices2.append([indice2, j])


equilibre_nash = [index for index in indice1 if index in indices2]

for nash in equilibre_nash:
    player1_strategy = nash[0]
    player2_strategy = nash[1]
    value = matrix[player1_strategy][player2_strategy]
    print(f"Équilibre de Nash pur : Joueur 1 choisit la stratégie {player1_strategy}, Joueur 2 choisit la stratégie {player2_strategy}, Valeur : {value}")