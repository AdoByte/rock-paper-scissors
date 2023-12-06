from random import choice


def play_rock():

    your_score = 0
    ai_score = 0

    while True:

        moves_dict = {'r':'rock', 'p':'paper', 's':'scissors'}
        valid_keys = list(moves_dict.keys())
        valid_values = list(moves_dict.values())

        user_input = input("Rock, Paper or Scissors.\nYou can use 'R', 'P' or 'S' >> ").lower()

        if user_input == 'exit':
            print('Thank you for playing')
            break

        if user_input not in valid_keys and user_input not in valid_values:
            print("Invalid move. . .")
            continue

        ai_input = choice(valid_keys)

        print("____________")
        if user_input in valid_keys:
            print(f"You played: {moves_dict[user_input]}", end=", ")
            print(f"AI played: {moves_dict[ai_input]}")
        elif user_input in valid_values:
            print(f"You played: {user_input}", end=", ")
            print(f"AI played: {moves_dict[ai_input]}")
        print("____________")

        if user_input == ai_input or user_input == moves_dict[ai_input]:
            print("It's a tie")
        elif user_input == 'r' and ai_input == 's' or user_input == 'rock' and moves_dict[ai_input]\
                == 'scissors':
            print("You win!")
            your_score+=1
        elif user_input == 's' and ai_input == 'p' or user_input == 'scissors' and moves_dict[ai_input]\
                == 'paper':
            print("You win!")
            your_score+=1
        elif user_input == 'p' and ai_input == 'r' or user_input == 'paper' and moves_dict[ai_input]\
                == 'rock':
            print("You win!")
            your_score+=1
        else:
            print("AI wins!")
            ai_score+=1
        print("____________")
        print(f"You:{your_score}  -  AI:{ai_score}")
        print()


if __name__ == '__main__':
    play_rock()


