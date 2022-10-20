import random

player_pos = 1
com_pos = 1

LEN = 30
PLAYER_CHAR = "@"
COM_CHAR = "P"

def board():
    print("."*(player_pos-1) + PLAYER_CHAR + "."*(LEN-player_pos) + "Goal")
    print("."*(com_pos-1) + COM_CHAR + "."*(LEN-com_pos) + "Goal")

board()
print("Game Start!")

while True:
    input("Enter _")
    player_pos = player_pos + random.randint(1, 6)
    if player_pos > 30:
        player_pos = 30
    board()
    if player_pos == 30:
        print("you win!")
        break

    input("Enter _")
    com_pos = com_pos + random.randint(1, 6)
    if com_pos > 30:
        com_pos = 30
    board()
    if com_pos == 30:
        print("computer win!")
        break
