import numpy as np 

blocks = open("input.txt", "r").read().split("\n\n")

locks, keys = [], []
for block in blocks:
    if block.startswith("#####\n"):
        block = block.replace("#", "1").replace(".", "0")
        m = np.array([list([int(bi) for bi in b]) for b in block.split("\n")])
        locks.append(tuple(np.sum(m[1:,:],axis=0)))
    else:
        block = block.replace("#", "0").replace(".", "1")
        m = np.array([list([int(bi) for bi in b]) for b in block.split("\n")])
        keys.append(tuple([5-i for i in np.sum(m[1:,::],axis=0)]))

locks = sorted(locks)
keys = sorted(keys)

print(len(locks), "locks")
print(len(keys), "keys")

def overlaps(lock, key):
    return any(np.array(lock)-(5-np.array(key)) > 0)

sol = 0
o = np.zeros((len(locks), len(keys)))
for i, l in enumerate(locks):
    for j, k in enumerate(keys):
        print("lock", l, "key", k, "overlap",  overlaps(l,k))
        if not overlaps(l,k): sol += 1 
print("solution",sol)

