import re

def find_mul(text):
    pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
    matches = re.findall(pattern, text)  
    return list(matches)

text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
# text = open("input.txt", "r").read()

matches = find_mul(text)
s = 0
enabled = True 

for m in matches:
    if m == "do()":
        enabled = True 
    elif m == "don't()":
        enabled = False 
    else:
        u, v = m.split("(")[1].split(")")[0].split(",")
        if enabled:
            s += int(u) * int(v)

print(s)
