input = """3   4
4   3
2   5
1   3
3   9
3   3""" # ... insert your input here

l = []
r = []
for line in input.split("\n"):
    lj, rj = line.split("   ")
    l.append(int(lj))
    r.append(int(rj))

# part 2 
s= 0
for xj in list(l):
    # print(xj, r.count(xj))
    s += xj*r.count(xj)
print("part2:", s)

# part 1 
l = sorted(l)
r = sorted(r)
s= 0
for j in range(len(l)):
    s += r[j] - l[j]
print("part1:", s)


