from world_generator import world_random_generator

ascii_deadOrAlive = {0 : "□",1 : "■"}


world_test2 =  [[0, 0, 1],
                [1, 0, 1],
                [1, 1, 1]]

def print_world(world:list[list[int]],
                update_mode:int = False) -> None:
    """GoL Terminal visulaization
    It visualize the world in form of □  and ■  for 0 and 1 (or dead and alive) status of the cell in the terminal

    Example:
        print_world([[0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1]])
        Output:
                □  □  ■  
                ■  □  ■  
                ■  ■  ■  

    Args:
        world: a list of list of binary integers showing the state of the GoL
        update_mode: Does it replace the print with the new print. Good to use with Loops and time.sleep to be able to see the output

    return:
        None
    """

    for i in range(len(world)):
        for j in range(len(world[0])):
            print(ascii_deadOrAlive[world[i][j]], " ", end="")
        print("")
    
    if (update_mode == True):
        for _ in range(len(world)):
            print("\033[F\033[K", end="")


#print_world(world_test2)


def test_print_world():
    import time
    for i in range(20):
        world = world_random_generator()
        print_world(world, update_mode = True)
        time.sleep(0.5)


# test_print_world()
