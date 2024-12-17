
import re

input = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

input = open("input.txt", "r").read()

global reg  # registry
global ptr # pointer
global output # output buffer

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

def run_prog(A_val): # runs the program
    global output 
    global ptr 
    global reg 
    ptr = 0
    output = []
    reg = [A_val, 0, 0]

    ops = {0: adv, 1: bxl, 2: bst, 3: jnz, 4:bxc, 5:out, 6:bdv, 7:cdv}
    while ptr < len(prog):
        opcode = prog[ptr]
        operand = prog[ptr+1]
        ops[opcode](operand)
        ptr += 2
    
    # if len(output) > 0:
    return output[:]

# part 2 

# find starting position
A_offset = 8**(len(prog)-1) - 10
output = []
while len(output) < len(prog):
    output = run_prog(A_offset)
    A_offset += 1

# try to find the last digits
def find_prog(cutoff, A_offset):
    k = 0
    A_offset -= 1
    while True:
        A_val = int(A_offset + k*8**cutoff)
        output = run_prog(A_val)
        if output[cutoff:] == prog[cutoff:]:
            print(">", ",".join(list(map(str, output))))
            break 
        else:
            k += 1
    return A_val

# step-wise brute force
A_offset = find_prog(len(prog)-2, A_offset)
A_offset = find_prog(len(prog)-6, A_offset)
A_offset = find_prog(len(prog)-8, A_offset)
A_offset = find_prog(len(prog)-10, A_offset)
A_final = find_prog(0, A_offset-1)
print(A_final)
