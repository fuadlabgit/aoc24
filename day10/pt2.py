input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

input = open("input.txt", "r").read()

import numpy as np 
m = np.array([list(i) for i in input.split("\n")])

ni, nj = m.shape 

starts = []
for i in range(ni):
    for j in range(nj):
        if m[i,j] == "0":
            starts.append((i,j))

def find_path(m, p0, p=None):
    if p is None: p = []
    curr = int(m[p0[0], p0[1]])
    p.append((p0[0], p0[1]))
    
    if curr == 9:
        return [p] # part 2
    
    trails = []
    for d in [(0,1), (0,-1), (1,0), (-1,0)]:
        p1 = (p0[0]+d[0],p0[1]+d[1])
        if 0 <= p1[0] < ni and 0 <= p1[1] < nj:
            nxt = int(m[p1[0], p1[1]])
            if nxt == curr+1: # selection rule for trail
                trails += find_path(m, p1, p[:])
    
    return trails 

score = 0
for start in starts:
    new_trails = find_path(m, start)
    # print(len(new_trails), "new trails")
    score += len(new_trails)
print(score)
