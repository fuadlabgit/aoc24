input = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

input = open("input.txt", "r").read()
# ------- Input parsing 

import numpy as np 
import sys 
REC_DEPTH = 800
sys.setrecursionlimit(REC_DEPTH)

m = np.array([list(l) for l in input.split("\n")])

def print_map(x, s=None, e=None, path=None):
    if s is not None:
        x[s[0], s[1]] = "S"
    if e is not None:
        x[e[0], e[1]] = "E"
    if path is not None:
        for p in path: 
            x[p[0], p[1]] = "x"
    s = ""
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            s += str(x[i,j])
        s +="\n"  
    print(s)
    
    if path is not None:
        for p in path: 
            x[p[0], p[1]] = "."
    
# ------- Puzzle 
import heapq

dmap = { "v": (1,0), ">": (0, 1), "<": (0, -1),   "^": (-1, 0)}

for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if m[i,j] == "S":
            s = (i,j)
        elif m[i,j] == "E":
            e = (i,j)
m[m=="S"] = "."
m[m=="E"] = "."

best_score = float("inf") # best score
seen = set() # memory of seen points
h = [(0, s[0], s[1], ">", [])] # priority queue of next points to visit

while h:
    score, startx, starty, last_d, p = heapq.heappop(h) # get next item

    if startx == e[0] and starty == e[1]:
        break # has lowest score when visited

    seen.add((startx, starty, last_d))
    p.append((startx, starty))

    if last_d == ">": next_dirs = ["^", "v", ">"] # cannot go reverse direction
    if last_d == "<": next_dirs = ["^", "v", "<"] 
    if last_d == "v": next_dirs = ["v", "<", ">"] 
    if last_d == "^": next_dirs = ["^" ,">", "<"]  
    
    for dir in next_dirs:
        nxt = (startx+dmap[dir][0], starty+dmap[dir][1])
        new_score = score+1 
        if last_d != dir:
            new_score = score + 1001
        if (m[nxt[0], nxt[1]] == "#") or ((nxt[0], nxt[1], dir) in seen):
            continue 
        heapq.heappush(h, (new_score, nxt[0], nxt[1], dir, p[:]))

print_map(m, s, e, path=p) 
print(score) 
