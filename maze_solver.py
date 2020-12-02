#!/usr/bin/env python
# -*- coding: utf-8 -*-

START, EXIT, VISITED, SOLUTION = '=>?!'
UPPERCASE = "".join(chr(x) for x in range(ord("A"), ord("A") + 26))
LOWERCASE = "".join(chr(x) for x in range(ord("a"), ord("a") + 26))
PATH = " " + START + LOWERCASE + UPPERCASE + "!"

code = """
class Maze():
    def __init__(self, ascii_maze, mname):
        self.maze = [list(x) for x in ascii_maze.splitlines()]
        self.start_y = [row.count(START) for row in self.maze].index(1)
        self.start_x = self.maze[self.start_y].index(START)
        self.mname = mname
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
                {0}
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
"""

if __name__ == "__main__":

    import sys
    from itertools import permutations
    sys.setrecursionlimit(sys.getrecursionlimit()*10)

    solutions = set()
    a = ['x-1,y', 'x+1,y', 'x,y-1', 'x,y+1']
    c = 1
    for p in permutations(a):

        s = 'if ('
        for pp in p:
            s += 'self.solve({0}, letters) or '.format(pp)
        s = s[:-4] + '):'

        exec compile(code.format(s), '', 'exec')
        maze = Maze(open('maze.txt').read(), c)
        if maze.solve():
            solution = ''.join(maze.letters)
            solutions.add(solution)
            print 'Permutation number {0}\n'.format(maze.mname)
            print code.format(s)[686:-332]
            print '\nSolution: {0}'.format(solution)
            print '-' * 20
        c += 1

    print '\nSolutions found:'
    print solutions
