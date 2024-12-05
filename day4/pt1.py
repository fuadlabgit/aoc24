
input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

input = open("input.txt", "r").read()

import numpy as np 
global tot_hits 
tot_hits = 0

def find_xmas(puzzle, x, y, d=None, s="X", path=None, hits=0):
    global tot_hits 

    if s == "XMAS":
        tot_hits += 1 
        return 
    elif len(s) >= 4: # beyond length of xmas cannot be 
        return 

    if d is None: # at first try all directions...
        d = [(-1, 1), (0, 1), (1, 1),
            (-1, 0),         (1, 0), 
            (-1, -1), (0, -1), (1, -1)]
    # else: keep search direction from previous search 

    if path is None: path = []
    path.append((x,y)) # elongate path 

    for dx, dy in d:

        u = x + dx 
        v = y + dy  # search steps

        if 0 <= u < len(puzzle) and 0 <= v < len(puzzle[0]): # check boundaries
            if puzzle[u, v] == "XMAS"[len(s)]:
                # recursive search
                find_xmas(puzzle, u, v, d=[(dx, dy)], s=s+puzzle[u,v], path=path, hits=hits)
                

puzzle = np.array([list(i) for i in input.split("\n")], dtype=str)

for x in range(len(puzzle)):
    for y in range(len(puzzle[0])):
        if puzzle[x, y] == "X":
            find_xmas(puzzle, x, y)

print(tot_hits)
