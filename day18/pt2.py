import numpy as np 
import heapq
import sys 

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

# N = 7  # dimension of map
# i_start = 0

input = open("input.txt", "r").read()
N = 71  # dimension of map
i_start = 2800 # 1024 NOTE modify to own needs 

m = np.zeros((N,N)) # map 

input_lines = input.splitlines()

# process first few bits
for i in input_lines[:i_start]: 
    t = list(map(int, i.split(",")))
    m[t[0], t[1]] = 1

s, e = (0,0), (N-1, N-1) # start and end of path
d, i = 0, i_start # path length so far , process index of bytes

dmap = { "v": (1,0), ">": (0, 1), "<": (0, -1),   "^": (-1, 0)}

while d >= 0 and i < len(input_lines): # slightly modified day 16 solution

    # drop new byte 
    t = list(map(int, input_lines[i].split(",")))
    m[t[0], t[1]] = 1
    i += 1 

    seen = set((0,0))        
    h = [(0, s[0], s[1], 0, [])]
    while h:
        score, startx, starty, d, p = heapq.heappop(h)
        p.append((startx, starty))
        seen.add((startx, starty))
        if startx == N-1 and starty == N-1:
            break # has lowest score when visited -> break loop
        
        for dir in [">" ,"<", "^", "v"]:
            nxt = (startx+dmap[dir][0], starty+dmap[dir][1])
            new_score = (score+1) + ((N-1)-nxt[0]) + ((N-1)-nxt[1])
            valid_spot = (0 <= nxt[0] <= N-1) and (0 <= nxt[1] <= N-1) and (m[nxt[0],nxt[1]] == 0)
            if (not valid_spot) or ((nxt[0], nxt[1]) in seen):
                continue 
            seen.add((nxt[0], nxt[1]))
            heapq.heappush(h, (new_score, nxt[0], nxt[1], d+1, p[:]))
    
    else: # loop did not break = no path found
        print(f"\n{t[0]},{t[1]}")
        break

    sys.stdout.write(f"Progress: {i}/{len(input_lines)}\r")

