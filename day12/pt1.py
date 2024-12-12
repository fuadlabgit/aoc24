input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

input = open("input.txt", "r").read()

import numpy as np 

ptypes = set(list(input))
ptypes.remove("\n")
# print(ptypes)

m = np.array([list(i) for i in input.split("\n")])
# print(m)

ni, nj = m.shape 

def explore(m, p, area):
    if len(area) == 0: 
        area.add(p)
    for q in [(p[0]+1, p[1]), (p[0]-1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)]:
        if 0 <= q[0] < ni and 0 <= q[1] < nj and q not in area:
            if m[q[0], q[1]] == m[p[0], p[1]]:
                area.add(q)
                explore(m, q, area)

score = 0
for ptype in ptypes:
    
    x, y = np.where(m==ptype)
    points = set([(x[i], y[i]) for i in range(len(x))])
    # print(points)

    areas = []
    while points:
        explored = set()
        start = points.pop()
        explore(m, start, explored)
        areas.append(set(explored))
        for e in explored:
            if e != start and e in points:
                points.remove(e)

    # print("areas", ptype, areas)

    for area in areas: 
        # compute area and perimeter 
        m_area = len(area)
        
        peri_points = []
        for p in area:
            for d in [(-1,0), (1,0), (0,1), (0,-1)]:
                q = (p[0]+d[0], p[1]+d[1])
                if q not in area or not(0 <= q[0] < ni and 0 <= q[1] < nj):
                    peri_points.append(q)
        m_peri = len(peri_points)

        print(ptype, " area = ", m_area, " perimeter =", m_peri)
        score += m_peri * m_area 

print(score)