from itertools import cycle

def mix(x, y): return x^y 
def prune(x): return x % 16777216

ops = cycle([lambda x: prune(mix(x, x*64)), lambda x: prune(mix(x, int(x/32))), lambda x: prune(mix(x, x*2048))])

def evolve(sn, n=2000):
    for _ in range(n*3):
        op = next(ops)
        sn = op(sn)
    return sn

input = open("input.txt", "r").read()

tot = 0
for line in input.splitlines():
    res = evolve(int(line))
    tot += res 
print(tot)
