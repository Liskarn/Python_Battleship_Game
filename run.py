import random

# Initialize the game board

board_size = 10
player_board = [["O"] * board_size for _ in range(board_size)]
enemy_board = [["O"] * board_size for _ in range(board_size)]


# Define the boat size


boat_size = 2


# Place the boats randomly on the board for the player


def place_player_boats():
    for _ in range(5):
        while True:
            x, y = random.randint(0, board_size - boat_size), random.randint(0, board_size - 1)
            positions = [(x + i, y) for i in range(boat_size)]
            if all(0 <= x < board_size and 0 <= y < board_size and player_board[x][y] == "O" for x, y in positions):
                for x, y in positions:
                    player_board[x][y] = "B"
                break


# Place the boats randomly on the board for the enemy AI


def place_enemy_boats():
    for _ in range(5):
        while True:
            x, y = random.randint(0, board_size - boat_size), random.randint(0, board_size - 1)
            positions = [(x + i, y) for i in range(boat_size)]
            if all(0 <= x < board_size and 0 <= y < board_size and enemy_board[x][y] == "O" for x, y in positions):
                for x, y in positions:
                    enemy_board[x][y] = "B"
                break

# Define a function to display the board


def print_board(board):
    print("   A B C D E F G H I J")
    for i, row in enumerate(board):
        print(i, " ".join(row))


# Define a function to get the player's guess


def get_player_guess():
    while True:
        guess = input("Enter your guess (e.g. A5): ")
        try:
            y, x = guess[0], int(guess[1:])
            return x, ord(y.upper()) - 65
        except:
            print("Invalid guess. Please try again.")


# Define a function for the enemy AI to make a random guess


def get_enemy_guess():
    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)
    return x, y


# Play the game


def play_game():
    print("Welcome to Battleship!")
    print("There are 5 boats hidden on the board.")
    print("Guess where the enemy's boats are by entering the coordinates.")
    print("Row first, then column.")
    print("You and the enemy will take turns guessing until all boats are sunk.")
    print_board(player_board)

    player_boats_sunk = 0
    enemy_boats_sunk = 0
    player_turn = True

    while player_boats_sunk < 5 and enemy_boats_sunk < 5:
        if player_turn:
            print("Player's turn:")
            x, y = get_player_guess()
            target_board = enemy_board
            target_boats_sunk = enemy_boats_sunk
        else:
            print("Enemy's turn:")
            x, y = get_enemy_guess()
            target_board = player_board
            target_boats_sunk = player_boats_sunk

        if target_board[x][y] == "B":
            print("Hit!")
            target_board[x][y] = "X"
            if all(target_board[i][y] == "X" for i in range(x, x + boat_size)):
                target_boats_sunk += 1
                print("You sunk a boat!")
        else:
            print("Miss!")
            target_board[x][y] = "-"

        player_turn = not player_turn
        print_board(player_board)
        print()

    print("Game over")
    if player_boats_sunk == 5:
        print("Congratulations! You won!")
    else:
        print("Sorry! You lost!")


# Main program flow


def main():
    place_player_boats()
    place_enemy_boats()
    play_game()


# Run the program


if __name__ == "__main__":
    main()