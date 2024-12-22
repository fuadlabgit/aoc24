import numpy as np 
from collections import deque 
from itertools import product 

"""
keypad 1:                  keypad 2:

+---+---+---+  -->  [x]        +---+---+ --> [x]
| 7 | 8 | 9 |                  | ^ | A |
+---+---+---+              +---+---+---+
| 4 | 5 | 6 |              | < | v | > |
+---+---+---+              +---+---+---+
| 1 | 2 | 3 |            
+---+---+---+              |
    | 0 | A |              v  [y]
    +---+---+

|
v  [y]

"""

input = """279A
286A
508A
463A
246A"""

pads = [  {(0,0):"7", (1,0):"8", (2,0):"9",
           (0,1):"4", (1,1):"5", (2,1):"6",
           (0,2):"1", (1,2):"2", (2,2):"3",
                      (1,3):"0", (2,3):"A"},  # numpad 1

          {           (1,0):"^", (2,0):"A",
            (0,1):"<",(1,1):"v", (2,1):">"},  # keypad 1
          
          {           (1,0):"^", (2,0):"A",
            (0,1):"<",(1,1):"v", (2,1):">"},  # keypad 2
          ]

def find(start, target, t=0):
    # find combinations to move to target from start 
    found = set()
    q = deque([(start[:], "")]) 
    best_score = float("inf")
    while q:
        pos, sequence = q.popleft() # popleft 

        if pads[t][pos] == target:
            best_score = min(best_score, len(sequence))
            if len(sequence) > best_score: break # find all possible shortest paths
            sequence += "A"
            found.add(sequence)
            continue
        
        for sdir, dir in {">": (1, 0), "v": (0,1), "<": (-1,0), "^": (0, -1)}.items(): 
            nxt = (pos[0]+dir[0], pos[1]+dir[1])
            nxt_seq = sequence + sdir
            if not nxt in pads[t]: continue
            q.append((nxt, nxt_seq))
    
    return found

# store move options of every keypad
global options
options = [{}, {}] 
for t in range(2):
    for coord in pads[t].keys():
        src = pads[t][coord]
        for coord2 in pads[t].keys():
            target = pads[t][coord2]
            if coord == coord2: 
                options[t][(src, target)] = ['A']
            else:
                options[t][(src, target)] = find(coord, target, t)

def lookup(string, keypad_id):
    global options 
    seqs = options[keypad_id]
    combis = [seqs[(x, y)] for x, y in zip("A" + string, string)] # zip (A029A, 029A) = (A, 0), (0, 2), (2, 9), (9, A)
    return ["".join(x) for x in product(*combis)] # product computes all possible combinations of the sequences to reach (A->0, 0->2 etc)

cache = {}
def explore(seq, max_id, robot_id=0):
    if (seq,robot_id) in cache: return cache[(seq, robot_id)]
    if robot_id == max_id: return len(seq) # < for part 2, set robo
    length = sum([min(explore(subseq, max_id, robot_id+1) for subseq in options[1][(x, y)]) for x, y in zip("A" + seq, seq)])
    cache[(seq, robot_id)] = length
    return length

input = """279A
286A
508A
463A
246A"""

# part 1
total = 0
for line in input.splitlines():
    inputs = lookup(line, 0)
    n = min([explore(s, max_id=2) for s in inputs]) 
    total += n * int(line[:-1])
print("part1:", total)

# part 2
cache = {}
total = 0
for line in input.splitlines():
    inputs = lookup(line, 0)
    n = min([explore(s, max_id=25) for s in inputs]) 
    total += n * int(line[:-1])
print("part2:", total)