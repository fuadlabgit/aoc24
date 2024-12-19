
input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

input = open("input.txt", "r").read()

# process inputs 
patterns = {}
for p in input.split("\n\n")[0].split(", "):
    if p[0] not in patterns: patterns[p[0]] = []
    patterns[p[0]].append(p)
designs = input.split("\n\n")[1].split("\n")

# solve part 1
def dfs(d, x=""):
    if len(x) == len(d) and x == d:
        return True     
    next_char = d[len(x)]
    if next_char in patterns:
        for p in patterns[next_char]:
            if len(x) + len(p) <= len(d) and x + p in d:
                if dfs(d, x + p): return True 
    return False

s = 0
for d in designs:
    if dfs(d):
        s += 1
print(s)
