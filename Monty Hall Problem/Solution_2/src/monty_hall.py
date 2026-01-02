from random import shuffle, choice


def monty_hall(switch_door:bool) -> bool:
    """This function simulates Monty Hall Problem

    :param switch_door: Shows you wanna switch door after the host reveals the goat or not
    :return: The winning state
    """
    doors = ['car', 'goat', 'goat']
    shuffle(doors)

    initial_choice = choice(range(3))

    if switch_door:
        revealed_doors = [i for i in range(3) if (i != initial_choice) and (doors[i] != 'car')]
        revealed_door = choice(revealed_doors)
        final_choice = [i for i in range(3) if (i != initial_choice) and (i != revealed_door)][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == 'car'


def simulate_problem(num_repetition:int) -> tuple[int, int]:
    """This function simulates the Monty Hall problem

    :param num_repetition: Number of repetitions you want the game repeats
    :return: Number of wins with switching door, Number of wins without switching door
    """
    num_wins_with_switching = sum([monty_hall(switch_door=True) for _ in range(num_repetition)])
    num_wins_without_switching = sum([monty_hall(switch_door=False) for _ in range(num_repetition)])

    return num_wins_with_switching, num_wins_without_switching


if __name__ == "__main__":
    simulate_problem(100)