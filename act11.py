matrice = []

for i in range(1, 6):
    l = [i, i ** 2] 
    matrice.append(l)
    
print(matrice)
# Pour obtenir une matrice plus lisible on peut l'afficher avec cette fonction :

for i in matrice:
    print(i)

#out: [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]
# [1, 1]
# [2, 4]
# [3, 9]
# [4, 16]
# [5, 25]
