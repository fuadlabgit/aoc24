
import re

input = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

input = open("input.txt", "r").read()

global reg 
reg = list(map(int, re.findall("Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)", input.split("\n\n")[0])[0]))
prog = list(map(int, input.split("\n\n")[1].split(": ")[1].split(",")))

def combo(y):
    global reg 
    if y in [0,1,2,3]:
        return y 
    elif y == 4:
        return reg[0]
    elif y == 5:
        return reg[1]
    elif y == 6: 
        return reg[2]

def adv(x):
    global reg
    reg[0] = int(reg[0]/ (2**combo(x)))

def bxl(x):
    global reg
    reg[1] = reg[1]^x

def bst(x): 
    global reg
    reg[1] = combo(x) % 8

def jnz(x): 
    global reg 
    global ptr
    if reg[0] == 0:
        return 
    ptr = x-2

def bxc(x):
    global reg 
    reg[1] = reg[1]^reg[2]

def out(x):
    global output
    output.append(combo(x) % 8)

def bdv(x): 
    global reg
    reg[1] = int(reg[0]/ (2**combo(x)))

def cdv(x):
    global reg 
    reg[2] = int(reg[0]/ (2**combo(x)))


if __name__ == "__main__":
    global ptr # pointer
    ptr = 0

    global output # output buffer
    output = []

    # for checking the examples: 
    #reg = [2024,2024,43690]
    #prog = [4,0 ]
    # print(reg, prog)

    ops = {0: adv, 1: bxl, 2: bst, 3: jnz, 4:bxc, 5:out, 6:bdv, 7:cdv}
    while ptr < len(prog):
        opcode = prog[ptr]
        operand = prog[ptr+1]
        ops[opcode](operand)
        ptr += 2

    print(",".join(list(map(str,output))))