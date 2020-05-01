import random


def guess_game():
    list_of_secret_numbers = [1, 2, 3, 4, 5]
    secret_number = random.choice(list_of_secret_numbers)
    match_count = 0
    match_limit = 3
    match_chances = 4
    while match_count < match_limit:
        match_chances -= 1
        print(f"Chances left: {match_chances}")
        user_input = int(input("Guess a number from 1 to 5: "))
        match_count += 1
        if user_input == secret_number:
            print("You won!")
            break
        elif user_input != secret_number:
            print("That was a wrong guess!")
    else:
        print("Do you want to play again???")
    exit_input = input("Press 'Y' for Yes or press 'N' for No... :")
    if exit_input.lower() == 'y':
        print("Rematching...")
        guess_game()
    elif exit_input.lower() == 'n':
        print("Bye,See you later :)")


guess_game()
