from random import choice

def play_rock():

    while True:
        moves_dict = {'r':'rock', 'p':'paper', 's':'scissors'}
        valid_moves_keys = list(moves_dict.keys())
        valid_moves_value = list(moves_dict.values())

        user_input = input("Rock, Paper or Scissors.\nYou can use 'R', 'P' or 'S' >> ").lower()

        if user_input == 'exit':
            print('Thank you for playing')
            break

        if user_input not in valid_moves_keys or user_input not in valid_moves_value:
            print("Invalid move. . .")
            continue

        ai_input = choice(valid_moves_keys)

        print("____________")
        if user_input in valid_moves_keys:
            print(f"You played: {moves_dict[user_input]}")
            print(f"AI played: {moves_dict[ai_input]}")
        elif user_input in valid_moves_value:
            print(f"You played: {user_input}")
            print(f"AI played: {moves_dict[ai_input]}")
        print("____________")

        if user_input == ai_input:
            print("It's a tie")
        elif user_input == 'rock' and ai_input == 'scissors':
            print("You win!")
        elif user_input == 'scissors' and ai_input == 'paper':
            print("You win!")
        elif user_input == 'paper' and ai_input == 'rock':
            print("You win!")
        else:
            print("AI wins!!!")

        print("____________")


if __name__ == '__main__':
    play_rock()




