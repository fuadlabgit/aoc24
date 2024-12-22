import numpy as np 
import heapq

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

# ------- Input parsing 
m = np.array([list(l) for l in input.split("\n")])

def print_map(x, s=None, e=None, path=None):
    if path is not None:
        for p in path: 
            x[p[0], p[1]] = "O"
    if s is not None:
        x[s[0], s[1]] = "S"
    if e is not None:
        x[e[0], e[1]] = "E"

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
dmap = { "v": (1,0), ">": (0, 1), "<": (0, -1),   "^": (-1, 0)}

for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if m[i,j] == "S":
            s = (i,j)
        elif m[i,j] == "E":
            e = (i,j)
m[m=="S"] = "."
m[m=="E"] = "."


# determine best path without cheating
seen = set()
h = [(0, s[0], s[1], tuple([float("inf")]*2), [])] # score, x, y, direction, cheat points, path tracker
while h:
    score, startx, starty, cheats, p = heapq.heappop(h) 
    if startx == e[0] and starty == e[1]:
        break 
     
    seen.add((startx, starty, *cheats))
    seen.add((startx, starty))
    p.append((startx, starty))

    next_dirs = ["^", "v", ">", "<"]
    
    for nxt_dir in next_dirs:
        nxt = (startx+dmap[nxt_dir][0], starty+dmap[nxt_dir][1])
        if not(0 <= nxt[0] < m.shape[0] and 0 <= nxt[1] < m.shape[1]): continue # out of bounds
        if (m[nxt[0], nxt[1]] == "#"): continue # is a wall and we dont cheat
        nxt_score = score+1
        nxt_cht = tuple(cheats)
        if ((*nxt, *cheats) in seen): continue # already visited
        heapq.heappush(h, (nxt_score, nxt[0], nxt[1], nxt_cht, p[:]))

best_score = score 
print("best score w/o cheating", best_score)

# determine paths with cheating 
import sys 

print("scores with cheating:")
seen = set()                      
h = [(0, s[0], s[1], tuple([float("inf")]*2), [])] # score, x, y, direction, cheat points, path tracker
solutions = []

while h:
    score, startx, starty, cheats, p = heapq.heappop(h) 
    if startx == e[0] and starty == e[1]:
        solutions.append((cheats, score))
        sys.stdout.write(f"{score}\r")
        # break
        if float("inf") in cheats:
            break 
        continue
    
    seen.add((startx, starty, *cheats))
    # seen.add((startx, starty))
    p.append((startx, starty))

    next_dirs = ["^", "v", ">", "<"]
    next_cheats = [False, True] if float("inf") in cheats else [False] # can cheat max. 2 times 
    
    for cheat in next_cheats:
        # print("net_cheats", next_cheats)
        for nxt_dir in next_dirs:
            nxt = (startx+dmap[nxt_dir][0], starty+dmap[nxt_dir][1])
            if not(0 <= nxt[0] < m.shape[0] and 0 <= nxt[1] < m.shape[1]): continue # out of bounds
            if (m[nxt[0], nxt[1]] == "#" and not cheat): continue # is a wall and we dont cheat
            
            nxt_score = score+1
            if cheat:
                nxt_cht = (nxt[0], nxt[1])
            else:
                nxt_cht = tuple(cheats)
            if ((*nxt, *nxt_cht) in seen): continue # already visited
            heapq.heappush(h, (nxt_score, nxt[0], nxt[1], nxt_cht, p[:]))


# count scores above 100
sol = 0

highest_score = max([s[1] for s in solutions])
savings = {} 
for s in solutions:
    sav = highest_score - s[1] - 2
    if sav <= 0: break 

    if sav not in savings: savings[sav] = 0
    savings[sav] += 1

    if sav > 100:
        sol += 1 

for k, v in savings.items():
    print(v, "cheats would save", k , "picoseconds")

print(sol)
