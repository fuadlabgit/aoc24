
input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""" # example input 

# input = open("input.txt", "r").read()

import numpy as np 
global tot_hits 
tot_hits = 0

def find_xmas2(p, x, y):
    global tot_hits 

    if not (1 <= x < len(p) and 1 <= y < len(p[0])-1):
        return 
     
    if p[x,y] == "A":
        print("found A",)
        try:
            """
            c1:   c2:     c3:     c4:

            M S   S S     M M     S M     
             A     A       A       A
            M S   M M     S S     S M
            """
            
            c1 = p[x-1, y+1] == "M" and p[x-1, y-1] == "M" and p[x+1, y+1] == "S" and p[x+1, y-1] == "S"
            c2 = p[x-1, y+1] == "S" and p[x-1, y-1] == "M" and p[x+1, y+1] == "S" and p[x+1, y-1] == "M"
            c3 = p[x-1, y+1] == "M" and p[x-1, y-1] == "S" and p[x+1, y+1] == "M" and p[x+1, y-1] == "S"
            c4 = p[x-1, y+1] == "S" and p[x-1, y-1] == "S" and p[x+1, y+1] == "M" and p[x+1, y-1] == "M"
            
            if c1 or c2 or c3 or c4:
                tot_hits += 1  
        except:
            pass

# puzzle map 
p = np.array([list(i) for i in input.split("\n")], dtype=str)

for x in range(len(p)):
    for y in range(len(p[0])):
        find_xmas2(p, x, y)

print(tot_hits)