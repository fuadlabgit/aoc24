input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

import numpy as np 

input = open("input.txt", "r").read()
steps = list(input.split("\n\n")[1].strip())[::-1]
while "\n" in steps: steps.remove("\n")

# scale the map
mapinput = []
for line in input.split("\n\n")[0].split("\n"):
    mj = []
    for l in line:
        lmap = {"#": "##", ".":"..", "@": "@.", "O": "[]"}
        mj+= list(lmap[l])
    mapinput.append(mj)
m = np.array(mapinput)

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

def try_move(m, p, dr, movelist=None):
    if movelist is None: movelist = []
    d = dmap[dr]
    p2 = p[0]+d[0], p[1]+d[1]
    if not ((0 <= p2[0] < m.shape[0]) and (0 <= p2[1] < m.shape[1])):
        return movelist
    if m[p2[0], p2[1]] == ".":
        movelist.append(p)
        return movelist 
    elif m[p2[0], p2[1]] == "#":
        movelist.append("#") # place blocker in movelist -> cannot move
        return movelist 
    elif m[p2[0], p2[1]] in ["[","]"]: # < different in part 2
        if dr in ["<", ">"]:
            movelist.append(p)
            try_move(m, p2, dr, movelist)
        else:
            movelist.append(p)
            try_move(m, p2, dr, movelist)
            if m[p2[0], p2[1]] == "]": p3 = (p2[0], p2[1]-1)
            elif m[p2[0], p2[1]] == "[": p3 = (p2[0], p2[1]+1)
            try_move(m, p3, dr, movelist)
    return movelist 

def move_bot(b):
    step = steps.pop()
    movelist = try_move(m, b, step)
    if not "#" in movelist:
        vals = [m[q[0], q[1]] for q in movelist]
        for i, q in enumerate(movelist): # remove old positions 
            m[q[0], q[1]] = "."
        for i, q in enumerate(movelist): # insert shifted positions
            m[q[0]+dmap[step][0], q[1]+dmap[step][1]] = vals[i]
        if len(movelist) > 0: b = (b[0]+dmap[step][0], b[1]+dmap[step][1]) # move bot position
    m[m=="@"] = "."
    return b

k = 0
while steps: # and k < 33:
    b = move_bot(b)
    k += 1 
print_map(m, b)

sol = 0
for i in range(m.shape[0]):
    for j in range(m.shape[1]):
        if m[i,j] == "[":
            sol += 100*i +j 
print(sol)