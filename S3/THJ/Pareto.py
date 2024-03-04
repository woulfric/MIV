import numpy as np

mat = np.array([[(3,2),(7,4),(4,0)],
               [(2,1),(1,3),(2,1)],
               [(1,4),(10,5),(0,2)]])

def pareto(mat):
    profiles = []
    for line in mat:
        for element in line:
            profiles.append(element)

    paretoDominants = [profiles[0]]
    for pro in profiles:
        for par in paretoDominants:
            if(pro[0]>par[0]):
                if (pro[1]>par[1]):
                    paretoDominants.append(pro)
                    paretoDominants.remove(par)
                else:
                    paretoDominants.append(pro)

                continue
            if(pro[1]>par[1]):
                if (pro[0]>par[0]):
                    paretoDominants.append(pro)
                    paretoDominants.remove(par)
                else:
                    paretoDominants.append(pro)

    return paretoDominants

print("Les profiles pareto sont : ",pareto(mat))