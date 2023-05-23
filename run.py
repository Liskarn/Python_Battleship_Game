import random

# Initialize the game board
board_size = 10
player_board = [["O"] * board_size for _ in range(board_size)]
enemy_board = [["O"] * board_size for _ in range(board_size)]

# Define the boat size
boat_size = 2

# Place the boats randomly on the board for the player
for _ in range(5):
    while True:
        x, y = random.randint(0, board_size - boat_size), random.randint(0, board_size - 1)
        positions = [(x + i, y) for i in range(boat_size)]
        if all(0 <= x < board_size and 0 <= y < board_size and player_board[x][y] == "O" for x, y in positions):
            for x, y in positions:
                player_board[x][y] = "X"
            break

# Place the boats randomly on the board for the enemy AI
for _ in range(5):
    while True:
        x, y = random.randint(0, board_size - boat_size), random.randint(0, board_size - 1)
        positions = [(x + i, y) for i in range(boat_size)]
        if all(0 <= x < board_size and 0 <= y < board_size and enemy_board[x][y] == "O" for x, y in positions):
            for x, y in positions:
                enemy_board[x][y] = "X"
            break

