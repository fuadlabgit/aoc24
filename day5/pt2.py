input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

input = open("input.txt", "r").read()
input1, input2 = input.split("\n\n")

ord = [] # extract page ordering rules 
for l in input1.split("\n"):
    u, v = l.split("|")
    ord.append((int(u), int(v))) # (int(u), int(v)))

u = [] # extract updates 
for l in input2.split("\n"):
    if l != "":
        u.append([int(li) for li in l.strip().split(",")])

def find_smaller(ord, x, found=None):
    if found is None:
        found = []
    if x not in found:
        found += [x]
        for o in ord:
            if x == o[1]:
                if o[0] not in found:
                    found = [o[0]] + found
                    found += find_smaller(ord, o[0], found) 
    return list(set(found))

def check_update(uj):
    for kk in range(len(uj)-1):
        preceeding = find_smaller(ord, uj[kk], None)
        for k in range(kk+1, len(uj)):
            if uj[k] in preceeding:
                return False 
    return True 

sol = 0
n = len(u) 
for j in range(n): 
    uj = u[j]
    if not check_update(uj):

        # pt2: sort correctly with bubble sort 
        nj = len(uj)
        for i in range(nj-1):
            for j in range(nj-i-1):
                if uj[j+1] in find_smaller(ord, uj[j], None):
                    uj[j], uj[j+1] = uj[j+1], uj[j]
        # ---
        
        im = int((len(uj)-1)/2) 
        sol += uj[im]

print(sol)
