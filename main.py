import random as rand


world = []

for i in range(10):
    world.append([])
    for j in range(10):
        world[i].append(rand.randint(0, 1))


print(world)
