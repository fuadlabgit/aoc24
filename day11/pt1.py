
input = "27 10647 103 9 0 5524 4594227 902936"
input = "125 17"

l = input.split()
l = list(map(int, l))

def transform(x):
    if x == 0: # zero -> 1
        return [1]
    elif len(str(x)) % 2 == 0: # even number -> split in two stones
        n = int(len(str(x))/2)
        x1 = int(str(x)[:n])
        x2 = int(str(x)[n:])
        return [x1, x2]
    return [x*2024] # none of the other apply -> *2024

n_blinks = 6
for k in range(n_blinks):
    new_l = []
    for i in range(len(l)):
        new_stones = transform(l[i])
        for stone in new_stones:
            new_l.append(stone)
    l = new_l

print(len(l))