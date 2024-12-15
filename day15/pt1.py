input = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

input = open("input.txt", "r").read()

import numpy as np 

steps = list(input.split("\n\n")[1].strip())[::-1]
while "\n" in steps: steps.remove("\n")

m = np.array([list(l) for l in input.split("\n\n")[0].split("\n")])


def print_map(x, b=None, d=None):
    if b is not None:
        x[b[0], b[1]] = "@"
    s = ""
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            s += str(x[i,j])
        s +="\n"  
    print(s)
    
dmap = {
    "v": (1,0),
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0)
}

for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if m[i,j] == "@":
            b = (i,j)
            break 

m[b[0], b[1]] = "."
#m[b[0], b[1]+1] = ">"
#m[b[0], b[1]-1] = "<"
#m[b[0]-1, b[1]] = "^"
#m[b[0]+1, b[1]] = "v"


def try_move(m, p, d):
    p2 = p[0]+d[0], p[1]+d[1]
    if not ((0 <= p2[0] < m.shape[0]) and (0 <= p2[1] < m.shape[1])):
        return False
    if m[p2[0], p2[1]] == ".":
        #print("<<", m[p[0], p[1]])
        m[p2[0], p2[1]] = m[p[0],p[1]]
        m[p[0], p[1]] = "."
        #print("ok")
        return True 
    elif m[p2[0], p2[1]] == "#":
        #print("*#")
        return False 
    elif m[p2[0], p2[1]] == "O":
        #print("*O")
        success = try_move(m, p2, d)
        if success:
            return try_move(m, p, d)
        else:
            return False 
    return True 

def move_bot(b):
    step = steps.pop()
    # print("step", step)
    success = try_move(m, b, dmap[step])
    m[m=="@"] = "."
    if success:
        b = (b[0]+dmap[step][0], b[1]+dmap[step][1])
    return b

while steps:
    b = move_bot(b)

print_map(m, b)

sol = 0
for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if m[i,j] == "O":
            sol += 100*i +j 
print(sol)