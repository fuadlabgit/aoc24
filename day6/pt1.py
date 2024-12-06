input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

input = open("input.txt", "r").read()

from itertools import cycle
import numpy as np 

# map 
m = np.array([list(c) for c in input.split("\n")]).T

ni = len(m)
nj = len(m[0])

# find guard 
dirmap = {
    "^": (0, -1), 
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0)
}
direction = cycle(dirmap.values())
d = next(direction) # current directions 

for x in range(ni):
    for y in range(nj):
        if m[x,y] in list(dirmap.keys()):
            guard = (x,y) # guard position
            while d != dirmap[m[x,y]]:
                d = next(direction) # guard direction
            m[x,y] = "." 

# move guard 
visited = set()

while True:
    if guard not in visited:
        visited.add(guard)

    # no obstacle
    q = guard[0] + d[0], guard[1]+d[1]
    
    if not (0 <= q[0] < ni and 0 <= q[1] < nj):
        break # exits
    if m[q[0], q[1]] != ".": #if m[*q] == "."
        d = next(direction) 
    else:
        guard = q # assign new position 
        
print(len(visited))