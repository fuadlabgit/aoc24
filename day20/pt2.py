import numpy as np 
import sys 

input = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

input = open("input.txt", "r").read()
 
m = np.array([list(l) for l in input.split("\n")])

for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if m[i,j] == "S": s = (i,j) 
        elif m[i,j] == "E": e = (i,j)
m[m=="S"] = "."
m[m=="E"] = "."

pathlen = {}
h = [(s[0], s[1], 0)]
while h:
    startx, starty, score = h[0]
    h = h[1:]
    pathlen[(startx, starty)] = score
    if startx == e[0] and starty == e[1]:
        continue
    dmap = { "v": (1,0), ">": (0, 1), "<": (0, -1), "^": (-1, 0)}
    for dx, dy in dmap.values():
        nxt = (startx+dx, starty+dy)
        if not(0 <= nxt[0] < m.shape[0] and 0 <= nxt[1] < m.shape[1]): continue
        if (m[nxt[0], nxt[1]] == "#"): continue 
        if nxt in pathlen: continue # < ensures shortest distance on the path to end point is stored!
        h.append((nxt[0], nxt[1], score+1))

tot = 0
sol = {}
mappoints = [(x,y) for x in range(m.shape[0]) for y in range(m.shape[1]) if m[x,y] != "#"]

grid_20x20 = []
for i in range(-20, 21):
    for j in range(-20, 21):
        d = abs(i) + abs(j)
        if 2 <= d <= 20:  grid_20x20.append((i,j,d))

count = 0
for p in mappoints:
    for dx, dy, d_cheat in grid_20x20:
        q = (p[0] + dx, p[1] + dy)
        if not(0 <= q[0] < m.shape[0] and 0 <= q[1] < m.shape[1]): continue
        if m[q[0], q[1]] == "#": continue
        
        cheat_dist = pathlen[q] + d_cheat # go alternative route and tunnel
        no_cheat_dist = pathlen[p] # stay on route without cheating
        diff = no_cheat_dist - cheat_dist
        if diff >= 100: count += 1 # -> q + tunnel is a valid cheat

print(count)
