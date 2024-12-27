input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

input = open("input.txt", "r").read()

import numpy as np 
from itertools import combinations

m = np.array([list(i) for i in input.split("\n")]).T
ni, nj = m.shape 

# def print_map(x):
#     s = ""
#     for i in range(len(x.T)):
#         for j in range(len(x.T[0])):
#             s += x.T[i,j] 
#         s += "\n"
#     print(s)

ats = {} # antennas sorted by frequency 
for i in range(ni):
    for j in range(nj):
        f = m[i,j]
        if f!= ".":
            if f not in ats: ats[f] = [] 
            ats[f].append((i,j))

ans = {} # antinodes positions
for f, positions in ats.items():
    print(f)
    ans[f] = [] 
    for p1, p2 in combinations(positions, r=2):
        print("   ", p1, p2)   
        d = p2[0]-p1[0], p2[1]-p1[1]
        
        # right-side ray
        finished = False
        j = 0
        while not finished:
            q1 = (p2[0]+j*d[0], p2[1]+j*d[1])
            if 0 <= q1[0] < ni and 0 <= q1[1] < nj:
                ans[f].append(q1)
                m[q1[0], q1[1]] = "#"
            else:
                finished = True 
            j += 1 
        
        # left-side ray
        finished = False 
        j = 0 
        while not finished:
            q2 = (p1[0]-j*d[0], p1[1]-j*d[1])
            if 0 <= q2[0] < ni and 0 <= q2[1] < nj:
                ans[f].append(q2)
                m[q2[0], q2[1]] = "#"
            else:
                finished=True 
            j += 1

# print_map(m)
# print(ats)
# print(list(combinations("ABC", r=2)))

unique_ans = set()
for k, v in ans.items():
    for vi in v: unique_ans.add(vi)
print(len(unique_ans))