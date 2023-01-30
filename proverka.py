cities = [('Москва', 1000), ('Рим', 2000), ('Самара', 250), ('Токио', 20000), ("Астрахань", 1232)]
print (sorted (cities))

print (sorted(cities, key=lambda q: q[1]))