
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
seen = {} 

def dfs(d, x="", options=0):
    if d in seen: return seen[d]
    if len(x) == len(d) and x == d:
        return 1     
    next_char = d[len(x)]
    if next_char in patterns:
        for p in patterns[next_char]:
            if len(x) + len(p) <= len(d) and x + p in d:
                options += dfs(d, x + p)
    seen[d] = options 
    return options 

s = 0
for d in designs:
    n_options = dfs(d)
    s += n_options
    # print(d, n_options)
print(s)
