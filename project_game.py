import os
import random

cmd = ""

grid_size = (25, 15)
grid = []
for y in range(grid_size[1]):
    grid.append([])
    for x in range(grid_size[0]):
        grid[y].append(" ")

# for i in range(grid_size[0]):
#     grid[0][i] = "#"
#     grid[-1][i] = "#"
# for i in range(grid_size[1]):
#     grid[i][0] = "#"
#     grid[i][-1] = "#"

grid_str = """
#########################
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                       #
#                      E#
#########################"""
x, y = 0, -1
for tile in grid_str:
    if tile != "\n":
        grid[y][x] = tile
        x += 1
    else:
        y += 1
        x = 0

player_pos = [1, 1]
player_pos_old = list(player_pos)
grid[player_pos[1]][player_pos[0]] = "P"
money = 0

collidable = ["#"]
no_of_enemies = int(input("Enter number of enemies: "))
random_enemy = []
for i in range(no_of_enemies):
    pos = [random.randint(5, grid_size[0] - 5), random.randint(5, grid_size[1] - 5)]
    random_enemy.append({"pos": pos})
    random_enemy[-1]["pos_old"] = pos
    grid[pos[1]][pos[0]] = "X"

no_of_coins = int(input("Enter number of coins: "))
for i in range(no_of_coins):
    pos = [random.randint(5, grid_size[0] - 5), random.randint(5, grid_size[1] - 5)]
    grid[pos[1]][pos[0]] = "C"

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    if cmd == "w":
        player_pos[1] -= 1
    if cmd == "a":
        player_pos[0] -= 1
    if cmd == "s":
        player_pos[1] += 1
    if cmd == "d":
        player_pos[0] += 1

    if grid[player_pos[1]][player_pos[0]] in collidable:
        player_pos = list(player_pos_old)

    if grid[player_pos[1]][player_pos[0]] == "C":
        money += 25

    if grid[player_pos[1]][player_pos[0]] == "E":
        print("You won!!!")
        break

    if grid[player_pos[1]][player_pos[0]] == "X":
        print("You lost.")
        break

    if player_pos != player_pos_old:
        grid[player_pos_old[1]][player_pos_old[0]] = " "
        grid[player_pos[1]][player_pos[0]] = "P"
    player_pos_old = list(player_pos)

    for i_ in range(len(random_enemy)):
        i = random_enemy[i_]
        r = random.randint(1,5)
        if r == 1:
            i["pos"][0] += 1
        if r == 2:
            i["pos"][0] -= 1
        if r == 3:
            i["pos"][1] += 1
        if r == 4:
            i["pos"][1] -= 1
        if grid[i["pos"][1]][i["pos"][0]] in collidable:
            i["pos"] = list(i["pos_old"])
        else:
            grid[i["pos"][1]][i["pos"][0]] = "X"
            grid[i["pos_old"][1]][i["pos_old"][0]] = " "
            i["pos_old"] = list(i["pos"])

    for y in grid:
        for x in y:
            print(x, end="")
        print()
    print("Money:", money)

    cmd = input()

input()