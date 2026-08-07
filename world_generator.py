import random as rand


def world_random_generator() -> list[list[int]]:
    world_test1 = []
    for i in range(10):
        world_test1.append([])
        for j in range(10):
            world_test1[i].append(rand.randint(0, 1))
    return world_test1




