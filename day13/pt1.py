import re
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, PULP_CBC_CMD

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
    puzzles.append(tuple(map(int, match))) # dx0, dy0, dx1, dy1, px, p

def cost(x0, x1):
    return [3*x0, x1]

s = 0
for i, puzzle in enumerate(puzzles, 1):
    prob = LpProblem("Integer_LP", LpMinimize)
    x0 = LpVariable("x0", lowBound=0, upBound=100, cat="Integer")
    x1 = LpVariable("x1", lowBound=0, upBound=100, cat="Integer")
    prob += lpSum(cost(x0, x1))
    prob += puzzle[0] * x0 + puzzle[2] * x1 == puzzle[4]
    prob += puzzle[1] * x0 + puzzle[3] * x1 == puzzle[5]
    prob.solve(PULP_CBC_CMD(msg=False))
    if LpStatus[prob.status] == "Optimal":
        s += sum(cost(x0.varValue, x1.varValue))

print(int(s))
