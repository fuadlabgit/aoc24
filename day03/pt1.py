import re

def find_mul(text):
    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern, text)  
    return list(matches)

text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
#text = open("input.txt", "r").read()

matches = find_mul(text)
s = 0
for m in matches:
    u, v = m.split("(")[1].split(")")[0].split(",")
    s += int(u) * int(v)

print(s)
