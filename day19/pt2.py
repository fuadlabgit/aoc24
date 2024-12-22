
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
patterns = {"r":[], "b":[], "w":[], "g":[], "u":[]}
for p in input.split("\n\n")[0].split(", "):
    if p[0] not in patterns: patterns[p[0]] = []
    patterns[p[0]].append(p)
designs = input.split("\n\n")[1].split("\n")

# part 2 requires a cache for already seen patterns...
finished = {}

def dfs(d, x="", ):
    if (d,x) in finished: return finished[(d,x)] # < important!
    if len(x) == len(d) and x == d:
        return 1
    next_char = d[len(x)]
    options = 0
    for p in patterns[next_char]:
        if len(x) + len(p) <= len(d) and x + p == d[:len(x+p)]:
            options += dfs(d, x + p)
    finished[(d,x)] = options # processing ends. remember this status for next time 
    return options

s = 0
for d in designs:
    s += dfs(d)
print(s)

# 642535800868438