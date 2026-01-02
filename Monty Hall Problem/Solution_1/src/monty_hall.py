from random import shuffle


def input_validator() -> int:
    """This function validates the user_first_choice

    :return: Number of the selected door
    """
    user_input = input("Please Choose a door between 0, 1, and 2: ")
    validated_choices = ["0", "1", "2"]
    if user_input not in validated_choices:
        print("Please enter a number between 0, 1, or 2")
        return input_validator()
    
    return int(user_input)


if __name__ == "__main__":
    CHOICES = ['goat', 'goat', 'car'] # All the possible choices
    shuffle(CHOICES)
    doors = list(enumerate(CHOICES))

    user_first_choice = input_validator()
    # Game logic
    print(f"Your choice is door number {user_first_choice}")
    user_first_choice = doors[user_first_choice]
    for door in doors:
        if (door != user_first_choice) and (door[1] != "car"):
            host_door = door
            break

    print(f"Behind door number {host_door[0]} is a goat")
    user_second_choice = input(
        f"""Do you wanna stay with the door number {user_first_choice[0]}
        or choose the other one? (y/any thing)"""
        )
    if user_second_choice.lower() == "y":
        user_second_choice = user_first_choice
        print(f"Behind door number {user_second_choice[0]} is a {user_second_choice[1]}")
    else:
        for door in doors:
            if (door != user_first_choice) and (door != host_door):
                user_second_choice = door
                print(f"You changed your choice to door number {user_second_choice[0]}")
                print(f"Behind door number {user_second_choice[0]} is a {user_second_choice[1]}")

    if user_second_choice[1] == "car":
        print("Yeahhhhhh you are the winner")
    else:
        print("Ohhhhh you loose")

# TODO: Test Cases
# TODO: Interactive dashboard using streamlit