import numpy as np 
import heapq
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
        if m[i,j] == "S":
            start = (i,j)
        elif m[i,j] == "E":
            end = (i,j)
m[m=="S"] = "."
m[m=="E"] = "."


def best_path(s, e):
    # determine best path without cheating
    seen = set()
    h = [(0, s[0], s[1], [])] # score, x, y, direction, path tracker
    while h:
        score, startx, starty, p = heapq.heappop(h) 
        if startx == e[0] and starty == e[1]:
            break 
        
        seen.add((startx, starty))
        p.append((startx, starty))

        next_dirs = ["^", "v", ">", "<"]
        dmap = { "v": (1,0), ">": (0, 1), "<": (0, -1),   "^": (-1, 0)}

        for nxt_dir in next_dirs:
            nxt = (startx+dmap[nxt_dir][0], starty+dmap[nxt_dir][1])
            if not(0 <= nxt[0] < m.shape[0] and 0 <= nxt[1] < m.shape[1]): continue # out of bounds
            if (m[nxt[0], nxt[1]] == "#"): continue # is a wall and we dont cheat
            if nxt in seen: continue # already visited
            heapq.heappush(h, (score +1, nxt[0], nxt[1], p[:]))
    return score , p

best_score, no_cheat_path = best_path(start, end)
pathlens = {p: i+1 for i, p in enumerate(no_cheat_path)}

sol = 0
for i_p, p in enumerate(no_cheat_path):
    cheat_score = pathlens[p] + 1

    for dir in [(2,0), (-2,0), (0,2), (0,-2)]: # < cheating possibilities
        qx, qy = p[0]+dir[0], p[1]+dir[1]

        if not(0 <= qx < m.shape[0] and 0 <= qy < m.shape[1]): continue
        if m[qx, qy] == "#": continue 

        if (qx, qy) in pathlens:
            no_cheat_score  = pathlens[(qx, qy)] 
        else:
            no_cheat_score,_ = best_path(start, (qx, qy))
        
        if cheat_score < no_cheat_score:
            diff = no_cheat_score - cheat_score
            if diff > 100: 
                sol += 1 
                print("cheat", qx, qy, "no cheat", no_cheat_score, "cheat", cheat_score, " saves", diff)
print("\n", sol)
