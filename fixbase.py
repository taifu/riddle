import random
UPPERCASE = "".join(chr(x) for x in range(ord("A"), ord("A") + 26))
LOWERCASE = "".join(chr(x) for x in range(ord("a"), ord("a") + 26))
maze = file("base.txt", "r").readlines()
for x, line in enumerate(maze):
    line = list(line)
    for y, car in enumerate(line):
        if x > 0 and y > 0 and x % 2 == 0 and y % 2 == 0:
            letters = UPPERCASE
            if car == " ":
                if (
                    (line[y - 1] == "|" and line[y + 2] == "|") or
                    (line[y - 2] == "|" and line[y + 1] == "|")
                    ):
                    letters += LOWERCASE
            elif car != "!":
                continue
            if random.randint(1, 100) > 30:
                line[y] = random.choice(letters)
        if line[y] == "!":
            line[y] = " "
    maze[x] = "".join(line)
file("maze.txt", "w").write("".join(maze))
