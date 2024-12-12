input = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

# input = open("input.txt", "r").read()

import numpy as np 

ptypes = set(list(input))
ptypes.remove("\n")

m = np.array([list(i) for i in input.split("\n")])
ni, nj = m.shape

def in_bounds(x):
    return  0 <= x[0] < ni and 0 <= x[1] < nj

def explore(m, p, area, corners):
    if len(area) == 0: area.add(p)

    # part 1: explore neighbors for area scanning
    for k, q in enumerate([(p[0]+1, p[1]), (p[0]-1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)]):
        if in_bounds(q):
            if m[q[0], q[1]] == m[p[0], p[1]]:
                if q not in area:
                    area.add(q)
                    explore(m, q, area, corners)

    # part 2: trace some more neighbors of the blocks
    neighbors = [False]*8
    for k, q in enumerate([(p[0]-1, p[1]-1), (p[0]-1, p[1]),(p[0]-1, p[1]+1),
                           (p[0], p[1]-1), (p[0], p[1]+1),
                           (p[0]+1, p[1]-1), (p[0]+1, p[1]),(p[0]+1, p[1]+1)]):
        if in_bounds(q):
            if m[q[0], q[1]] == m[p[0], p[1]]:
                neighbors[k] = True

    """
    outward corners 
      012
      3.4
      567

    +---> (y)
    |
    v
    (x)

    a     b   c  d
    EE. .EE ... ... 
    EX. .XE EX. .XE 
    ... ... EE. .EE 
    """
    if (not neighbors[1] and not neighbors[3]): 
        corners.append((2*p[0], 2*p[1]) )
    if (not neighbors[1] and not neighbors[4]): 
        corners.append((2*p[0], 2*p[1]+1) )
    if (not neighbors[3] and not neighbors[6]): 
        corners.append((2*p[0]+1, 2*p[1]) )
    if (not neighbors[4] and not neighbors[6]): 
        corners.append((2*p[0]+1, 2*p[1]+1) )

    """
    inward corners
      012
      3.4
      567

    +---> (y)
    |
    v
    (x)

    e     f    g   h
    ...  ...  ox.  .xo
    .xx  xx.  xx.  .xx
    .xo  ox.  ...  ...
    """
    if (neighbors[3] and neighbors[1] and (not neighbors[0])):
        corners.append((2*p[0], 2*p[1]) )
    if (neighbors[1] and neighbors[4] and (not neighbors[2])):
        corners.append((2*p[0], 2*p[1]+1) )
    if (neighbors[3] and neighbors[6] and (not neighbors[5])):
        corners.append((2*p[0]+1, 2*p[1]) )
    if (neighbors[4] and neighbors[6] and (not neighbors[7])): 
        corners.append((2*p[0]+1, 2*p[1]+1) )


score = 0
for ptype in ptypes:

    x, y = np.where(m==ptype)
    points = set([(x[i], y[i]) for i in range(len(x))])

    areas = []
    all_corners = []
    while points: # process all the points 
        explored, corners = set(), []
        start = points.pop()
        explore(m, start, explored, corners)
        areas.append(set(explored))
        all_corners.append(set(corners))
        for e in explored:
            if e != start and e in points:
                points.remove(e)
    for i, area in enumerate(areas): # process all the joined areas
        corners = all_corners[i]
        m_area = len(area)
        m_peri = len(corners) 
        score += m_peri * m_area 

print(score)