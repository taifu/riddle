import random
UPPERCASE = "".join(chr(x) for x in range(ord("A"), ord("A") + 26))
LOWERCASE = "".join(chr(x) for x in range(ord("a"), ord("a") + 26))
maze = file("base.txt", "r").readlines()
for x, line in enumerate(maze):
    line = list(line)
    for y, car in enumerate(line):
        if car in "! " and line[y - 1] not in "! " and line[y + 1] not in "! ":
            letters = UPPERCASE
            if car != "!":
                letters += LOWERCASE
            if random.randint(1, 100) > 30:
                car = random.choice(letters)
        if car == "!":
            car = " "
        line[y] = car
    maze[x] = "".join(line)
file("maze.txt", "w").write("".join(maze))
