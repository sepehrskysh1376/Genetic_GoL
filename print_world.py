import random as rand

ascii_deadOrAlive = {0 : "□",1 : "■"}

world_test1 = []

for i in range(10):
    world_test1.append([])
    for j in range(10):
        world_test1[i].append(rand.randint(0, 1))

world_test2 =  [[0, 0, 1],
                [1, 0, 1],
                [1, 1, 1]]

def print_world(world:list[list[int]],
                mode:int = 1) -> None:
    for i in range(len(world)):
        for j in range(len(world[0])):
            print(ascii_deadOrAlive[world[i][j]], " ", end="")
        print("")


print_world(world_test1)
