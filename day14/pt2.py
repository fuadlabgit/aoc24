input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

import numpy as np 
input = open("input.txt", "r").read()

bots = []
for l in input.split("\n"):
    p = list(l.split()[0].split("=")[1].split(","))
    v = list(l.split()[1].split("=")[1].split(","))
    p = [int(p[0]), int(p[1])]
    v = [int(v[0]), int(v[1])]
    # print(p,v)
    bots.append((p,v))

# max_x, max_y = 11, 7 
max_x, max_y = 101, 103
import sys 
import time 

best_sf = np.inf 

all_str = ""

for t in range(100_000):
    m = np.zeros((max_x, max_y), dtype= "int")

    for k_b, b in enumerate(bots):
        m[b[0][0], b[0][1]] += 1
        
        b[0][0] += b[1][0]
        b[0][1] += b[1][1]

        if b[0][0] >= max_x:
            b[0][0] = b[0][0]-max_x
        if b[0][1] >= max_y:
            b[0][1] = b[0][1]-max_y
        if b[0][0] < 0:
            b[0][0] = max_x+b[0][0]
        if b[0][1] < 0:
            b[0][1] = max_y+b[0][1]

    # compute safety factor
    q1, q2, q3, q4 = 0,0,0,0
    q1 = np.sum(m[0:int(max_x/2-0.5), 0:int(max_y/2-0.5)])
    q2 = np.sum(m[int(max_x/2+0.5):, 0:int(max_y/2-0.5)])
    q3 = np.sum(m[0:int(max_x/2-0.5), int(max_y/2+0.5):])
    q4 = np.sum(m[int(max_x/2+0.5):, int(max_y/2+0.5):])
    q5 = np.sum(m[0:10, 0:10])
    q6 = np.sum(m[-10:, 0:10])
    
    sf = q1*q2*q3*q4 # + q4 + q5
    sys.stdout.write(f"t={t}, {sf}\r")
    
    if sf < best_sf:

        s = ""
        for j in range(max_y):
            for i in range(max_x):
                ms = str(m[i,j])
                if ms == "0": ms = "."
                s+= ms #+ " "

            s+= "\n"
        
        best_sf = sf
        print(s)
        print("is the solution", t, "?")

with open("output.txt", "w") as file:
    file.write(all_str)
