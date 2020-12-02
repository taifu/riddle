START, EXIT, VISITED, SOLUTION = '=>?!'
UPPERCASE = "".join(chr(x) for x in range(ord("A"), ord("A") + 26))
LOWERCASE = "".join(chr(x) for x in range(ord("a"), ord("a") + 26))
PATH = " " + START + LOWERCASE + UPPERCASE + "!"
class Maze():
    def __init__(self, ascii_maze):
        self.maze = [list(x) for x in ascii_maze.splitlines()]
        self.start_y = [row.count(START) for row in self.maze].index(1)
        self.start_x = self.maze[self.start_y].index(START)
        self.letters = []

    def __repr__(self):
        return "\n".join("".join(line) for line in self.maze)

    def solve(self, x = None, y = None, letters = []):
        try:
            if x == None:
                x, y = self.start_x, self.start_y
            if self.maze[y][x] in PATH:
                added = False
                if self.maze[y][x] in LOWERCASE:
                    letters.append(self.maze[y][x])
                    added = True
                self.maze[y][x] = VISITED
                if (self.solve(x+1, y, letters) or self.solve(x, y+1, letters) or
                    self.solve(x-1, y, letters) or self.solve(x, y-1, letters)):
                    self.maze[y][x] = SOLUTION
                    return True
                elif added:
                    letters.pop(len(letters) - 1)
            elif self.maze[y][x] == EXIT:
                self.letters = letters
                return True
        except IndexError:
            pass
        return False

ASCII_MAZE = """
+-------------+
|     |   | | |
| | +-+ --+ | |
| | |       | |
| |   +-- | | |
| | | |   | | >
|   | | | | | |
+---+ | | | | |
=     | | |   |
+-----+-+-+---+
"""

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10000)
    if len(sys.argv) > 1:
        maze = Maze(open(sys.argv[1]).read())
    else:
        maze = Maze(ASCII_MAZE)
    if maze.solve():
        print "".join(maze.letters)
