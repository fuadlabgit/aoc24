input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

input = open("input.txt", "r").read()

from itertools import product

# part 1:
ops = [lambda x, y: x+y, lambda x, y: x*y] # possible operations
# part 2:
# ops = [lambda x, y: x+y, lambda x, y: x*y, lambda x, y: int(str(x) + str(y))] # possible operations 

s = 0
for line in input.split("\n"):
    v, x = line.split(":")
    v = int(v)
    x = list(map(int, x.split()))
    combis = list(product(ops, repeat=len(x)-1))
    print(v, x) # print progess (optional)
    
    for combi in combis:
        result = x[0]
        for j, xj in enumerate(x[1:]):
            result = combi[j](result, xj)
        if result == v: # result is ok -> add the result and start with the next 
            s += v
            break

print(s)