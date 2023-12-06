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

        print()
        print(f"You played: {user_input}")
        print(f"AI played: {ai_input}")
        print()

        






