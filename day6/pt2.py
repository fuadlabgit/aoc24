from itertools import cycle
import numpy as np 

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
m = np.array([list(c) for c in input.split("\n")]).T # map

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

start_pos = tuple(guard)
start_dir = tuple(d)

# def print_map(x):
#     s = ""
#     for i in range(len(x.T)):
#         for j in range(len(x.T[0])):
#             s += x.T[i,j] 
#         s += "\n"
#     print(s)

# pt2
s = 0
for x in range(ni):
    for y in range(nj):
        
        progress = int(100*(x + y*ni)/(ni * nj))
        print("progress:", progress)

        if (x,y) == start_pos:
            continue 
        
        m[m!= "#"]  = "."
        m[start_pos[0], start_pos[1]] = "A"

        if m[x, y] != "#" and (x,y) != start_pos:
            m[x, y] = "O"
            
            visited = set()
            is_loop = False 
            while True: 
                new_pos = (guard[0], guard[1], d[0], d[1])
                if new_pos in visited:
                    is_loop = True 
                    break 
                visited.add(new_pos)
                
                q = guard[0] + d[0], guard[1]+d[1]
                if not (0 <= q[0] < ni and 0 <= q[1] < nj):
                    break 
                if m[q[0], q[1]] in ["O", "#"]: 
                    d = next(direction) 
                else:
                    guard = q # assign new position 
            
            guard = start_pos # restore starting condition 
            while d != start_dir:
                d = next(direction)

            if is_loop:
                s += 1 
                # print_map(m)
            
            m[x, y] = "." # restore previous state

print(s)