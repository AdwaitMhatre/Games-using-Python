# global variables
again = "y"
while again == "y":
    board = ["-" for x in range(1,10)]

    game_still_working = True

    winner = None

    current_player = "X"

# Functions
    def board_print():
          print(board[0] + " | " + board[1] + " | " + board[2])
          print("---------")
          print(board[3] + " | " + board[4] + " | " + board[5])
          print("---------")
          print(board[6] + " | " + board[7] + " | " + board[8])

    def play_game():
    # initial board
          board_print()

          global game_still_working

          while game_still_working:

                player_turn(current_player)

                check_the_game()

                change_player()

          if winner == "X" or winner == "O":
              print("Player " + winner + " won!")
          elif winner == None:
              print("Tie!")

    def player_turn(player):
        print(player + "'s turn")
        move = input("Choose a position between 1-9: ")

        while move not in ["1","2","3","4","5","6","7","8","9"]:
            move = input("Please enter a value in given range: ")
        move = int(move) - 1
        if board[move] != "-":
            move = input("This space is already occupied,please try another position: ")
            move = int(move) - 1
        board[move] = player
        board_print()

    def check_the_game():
        check_if_win()
        check_if_tie()

    def check_if_win():
        global winner
        global game_still_working

        W1 = board[0] == board[1] == board[2] != "-"
        W2 = board[3] == board[4] == board[5] != "-"
        W3 = board[6] == board[7] == board[8] != "-"
        W4 = board[0] == board[3] == board[6] != "-"
        W5 = board[1] == board[4] == board[7] != "-"
        W6 = board[2] == board[5] == board[8] != "-"
        W7 = board[0] == board[4] == board[8] != "-"
        W8 = board[6] == board[4] == board[2] != "-"

        if W1 or W2 or W3 or W4 or W5 or W6 or W7 or W8:
            game_still_working = False
        if W1:
            winner = board[0]
        elif W2:
            winner = board[3]
        elif W3:
            winner = board[6]
        elif W4:
            winner = board[0]
        elif W5:
            winner = board[1]
        elif W6:
            winner = board[2]
        elif W7:
            winner = board[0]
        elif W8:
            winner = board[6]

    def check_if_tie():
        global winner
        global game_still_working
        W1 = board[0] == board[1] == board[2] != "-"
        W2 = board[3] == board[4] == board[5] != "-"
        W3 = board[6] == board[7] == board[8] != "-"
        W4 = board[0] == board[3] == board[6] != "-"
        W5 = board[1] == board[4] == board[7] != "-"
        W6 = board[2] == board[5] == board[8] != "-"
        W7 = board[0] == board[4] == board[8] != "-"
        W8 = board[6] == board[4] == board[2] != "-"

        if "-" not in board:
            game_still_working = False
            if W1 or W2 or W3 or W4 or W5 or W6 or W7 or W8:
                if W1:
                    winner = board[0]
                elif W2:
                    winner = board[3]
                elif W3:
                    winner = board[6]
                elif W4:
                    winner = board[0]
                elif W5:
                    winner = board[1]
                elif W6:
                    winner = board[2]
                elif W7:
                    winner = board[0]
                elif W8:
                    winner = board[6]
            else:
                winner = None

    def change_player():
        global current_player

        if current_player == "X":
            current_player = "O"
        elif current_player == "O":
            current_player = "X"

    def play_pc():
        global winner
        global game_still_working
        board_print()

        while game_still_working:
            your_turn()
            check_the_game()
            computer_turn()
            check_the_game()

        if winner == "X":
            print("You won!")
        elif winner == "O":
            print("Computer won!")
        elif winner == None:
            print("Tie!")

    def your_turn():
        print("Your turn ")
        move1 = input("Choose a position between 1-9: ")
        while move1 not in ["1","2","3","4","5","6","7","8","9"]:
            move1 = input("Please select a postion in the given range: ")
            move1 = int(move1) - 1
        if board[move1] != "-":
            move1 = input("This space is already occupied. Please try another position: ")
            move1 = int(move1) - 1
        board[move1] = "X"
        board_print()

    def computer_turn():
        import random
        print("Computer's turn")
        possible_moves = [x for x, element in enumerate(board) if element == "-" and x != 0]
        if possible_moves == []:
            possible_moves = ["0"]
        else:
            move2 = random.choice(possible_moves)
            board[move2] = "O"
            board_print()

    def main():
        z = input("Enter y to play with a player or Enter n to play with computer: ")
        if z == "y":
            play_game()
        elif z == "n":
            play_pc()
        else:
            z = input("Please enter valid input: ")

    print("Welcome to Tic Tac Toe")
    print("----------------------")
    main()
again = input("Enter y to play")
