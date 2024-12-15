import re
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, PULP_CBC_CMD
import sys 
import numpy as np 

# Input string
data = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

data = open("input.txt", "r").read()

pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
matches = re.findall(pattern, data)

puzzles = []
for match in matches:
    puzzles.append(tuple(map(int, match))) # dx0, dy0, dx1, dy1, px, py

"""
m* dxa + n*  dxb = px 
m* dya + n* dyb  = py 

n = (py - m* dya)/ dyb 
m* dxa + [(py - m* dya)/ dyb] *dxb  = px 
m * dxa - m * (dya/dyb) * dxb + py * dxb/dyb = px
m * (dxa - (dya/dyb)*dxb) = px - py * dxb/dyb
m = (px - (py * dxb/dyb))/(dxa - (dya/dyb)*dxb)
m = (px * dyb - py * dxb)/(dxa* dyb - dxb * dya)

"""
s = 0
for i, puzzle in enumerate(puzzles, 1):
    # print(puzzle)
    dxa, dya, dxb, dyb, px, py = puzzle
    px += 10000000000000 # 1000
    py += 10000000000000 # 1000
    m = (px * dyb - py * dxb)/(dxa* dyb - dxb * dya)
    m2 = (px - ((py * dxb)/dyb))/(dxa - (dya/dyb)*dxb)
    n = (py - m*dya)/dyb 
    #print(m,m2, np.round(m2) - m, n)
    if abs(np.round(m) - m) < 0.01 and abs(np.round(n) - n) < 0.01:
        #if m <= 100 and n <= 100:
        s += 3*m + n

sys.stdout.write("\n")
print(int(s))

# 217280895 too low
# 67715264300000 too low 
# 60655980690000
# 65836014010000
# 71824293120000
# 64690114780000
# 59488379700000
# 60864640380000
# 67804225233000