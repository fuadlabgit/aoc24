
input = open("input.txt", "r").read().split("\n\n")[1]

formulas = {z: (op, x, y) for x, op, y, z in [line.replace(" -> ", " ").split() for line in input.splitlines()]}

def check_xy(wire, num):
    return sorted([formulas[wire][1],formulas[wire][2]]) == ["x%02i"%num, "y%02i"%num]

def xor(i, num):
    return i in formulas and formulas[i][0] == "XOR" and check_xy(i, num)

def check_carry(wires, num):
    direct_carry = lambda i, num: i in formulas and (formulas[i][0] == "AND" and check_xy(i, num))
    recarry = lambda i, num: i in formulas and formulas[i][0] == "AND" and any([xor(i,num) and carry_bit(j, num) for i, j in [(formulas[i][1],formulas[i][2]), (formulas[i][2],formulas[i][1])]])
    return any([direct_carry(i, num ) and recarry(j, num) for i, j in [(wires[1],wires[2]), (wires[2],wires[1])]])

def carry_bit(i, num):
    return  i in formulas and ((num==1 and formulas[i][0] == "AND" and check_xy(i, 0)) or (num!= 1 and formulas[i][0] == "OR" and check_carry(formulas[i],num-1))) 

def verify(num):
    wire = "z%02i"%num
    if wire not in formulas: return False
    op, a, b = formulas[wire]
    if op != "XOR": return False
    if num == 0: return check_xy(wire, num) 
    return any([xor(i, num) and carry_bit(j, num) for i, j in [(a,b),(b,a)]]) 

def try_swap(gate1, gate2, digit):
    formulas[gate1], formulas[gate2] = formulas[gate2], formulas[gate1]
    digit0 = digit
    while verify(digit): digit += 1
    if digit > digit0: return digit, True
    formulas[gate1], formulas[gate2] = formulas[gate2], formulas[gate1]
    return digit0, False

digit = 0
sol = []
for _ in range(4):
    while verify(digit): digit += 1
    for g1, g2 in [(gate1, gate2) for gate1 in formulas for gate2 in formulas if gate1 != gate2]:
        digit, success = try_swap(g1, g2, digit)
        if success: break 
        else: continue
        break
    sol += [g1, g2]

print(",".join(sorted(sol)))