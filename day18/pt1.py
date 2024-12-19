input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

import numpy as np 
import heapq

N = 7  # dimension of map
n_max = 12 # max bits to read 

input = open("input.txt", "r").read()
N = 71  # dimension of map
n_max = 1024 # max bits to read

m = np.zeros((N,N)) # map 

# start and end of path
s = (0,0)
e = (N-1,N-1)

# process corrupted bits
for i in input.split("\n")[:n_max]:
    t = list(map(int, i.split(",")))
    m[t[0], t[1]] = 1

def print_map(y, path=None):
    x = y.copy()
    if path:
        for p in path:
            x[p[0],p[1]] = -1
    s = ""
    for i in range(x.shape[1]):
        for j in range(x.shape[0]):
            if x[j,i] == 0:
                s+= "."
            elif x[j,i] == -1:
                s+= "O"
            else:
                s += "#"
        s+="\n"
    print(s)

# slightly modified day 16 solution
dmap = { "v": (1,0), ">": (0, 1), "<": (0, -1),   "^": (-1, 0)}
seen = set((0,0))        # memory of seen points
h = [(0, s[0], s[1], 0, [])] # priority queue of next points to visit

while h:
    score, startx, starty, d, p = heapq.heappop(h)
    p.append((startx, starty))
    seen.add((startx, starty))
    if startx == N-1 and starty == N-1:
        break # has lowest score when visited
    
    for dir in [">" ,"<", "^", "v"]:
        nxt = (startx+dmap[dir][0], starty+dmap[dir][1])
        new_score = (score+1) + ((N-1)-nxt[0]) + ((N-1)-nxt[1])
        valid_spot = (0 <= nxt[0] <= N-1) and (0 <= nxt[1] <= N-1) and (m[nxt[0],nxt[1]] == 0)
        if (not valid_spot) or ((nxt[0], nxt[1]) in seen):
            continue 
        seen.add((nxt[0], nxt[1]))
        heapq.heappush(h, (new_score, nxt[0], nxt[1], d+1, p[:]))

print_map(m, path=p)
print(d)
