maze = list(file("empty.txt", "r").readlines())
new_maze = []
for x, line in enumerate(maze):
    new_line = ""
    for y in range(1, len(line) - 2, 3):
        new_line += line[y-1:y+1]
    new_line += line[-2:]
    new_maze.append(new_line)
file("notempty.txt", "w").write("".join(new_maze))

for x, line in enumerate(new_maze):
    if x == 0 or x == len(new_maze) - 1:
        continue
    new_line = line[0]
    for y in range(1, len(line) - 1):
        if "x" == line[y] == line[y + 1] == new_line[y - 1] == new_maze[x + 1][y - 1] == new_maze[x + 1][y] == new_maze[x + 1][y + 1]:
            new_line += "|"
        elif line[y] == "_":
            new_line += "-"
        else:
            new_line += line[y]
    new_line += line[-1]
    new_maze[x] = new_line

for x, line in enumerate(new_maze):
    if x == 0 or x == len(new_maze) - 1:
        continue
    new_line = line[0]
    for y in range(1, len(line) - 1):
        if line[y] == "|" and (line[y - 1] == "-" or line[y + 1] == "-"):
            new_line += "+"
        elif line[y] == "-" and new_maze[x + 1][y] == "|":
            new_line += "+"
        elif line[y] == " " and line[y - 1] == "-" and new_maze[x + 1][y] == "|":
            new_line += "+"
        elif line[y] == " " and line[y + 1] == "-" and new_maze[x - 1][y] == "|":
            new_line += "+"
        elif line[y] == " " and line[y - 1] == "-" and new_maze[x - 1][y] == "|":
            new_line += "+"
        else:
            new_line += line[y]
    new_line += line[-1]
    new_maze[x] = new_line
file("notempty.txt", "w").write("".join(new_maze))

