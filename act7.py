tab = [1, 2, 3, 4, 5, 6]

print("1:" + str([i ** 2 for i in tab]))

# Alternativement

def incremente_tableau(tableau):
    car = []
    for i in tableau:
        car.append(i ** 2)
    return car
    
print("2:" + str(incremente_tableau(tab)))

#out :
# 1:[1, 4, 9, 16, 25, 36]
# 2:[1, 4, 9, 16, 25, 36]
