from random import choice

def play_rock():

    while True:
        valid_moves = ['rock', 'paper', 'scissors']
        user_input = input("Rock, Paper or Scissors >> ").lower()

        if user_input == 'exit':
            print('Thank you for playing')
            break

        if user_input not in valid_moves:
            print("Invalid move. . .")
            continue

        ai_input = choice(valid_moves)

        print("____________")
        print(f"You played: {user_input}")
        print(f"AI played: {ai_input}")
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





