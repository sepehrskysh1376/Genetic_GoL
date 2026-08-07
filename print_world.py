import time
import random as rand

ascii_deadOrAlive = {0 : "□",1 : "■"}


def world_random_generator() -> list[list[int]]:
    world_test1 = []
    for i in range(10):
        world_test1.append([])
        for j in range(10):
            world_test1[i].append(rand.randint(0, 1))
    return world_test1

world_test2 =  [[0, 0, 1],
                [1, 0, 1],
                [1, 1, 1]]

def print_world(world:list[list[int]],
                update_mode:int = False) -> None:

    for i in range(len(world)):
        for j in range(len(world[0])):
            print(ascii_deadOrAlive[world[i][j]], " ", end="")
        print("")
    
    if (update_mode == True):
        for _ in range(len(world)):
            print("\033[F\033[K", end="")
    
for i in range(10):
    world = world_random_generator()
    print_world(world, update_mode = True)
    time.sleep(0.5)

