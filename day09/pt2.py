
dm = list("2333133121414131402") # disk map
#dm = list(open("input.txt", "r").read())

# create file block by decompressing disk map
spaces = []  # index of spaces 
numbers = [] # index of numbers 

block = [] # block data 
j = 0
block_id = 0 
k = 0
while j < len(dm):
    n = int(dm[j]) 
    if j % 2 == 0:
        if n > 0:
            block += [str(block_id)]*n
            block_id += 1
            numbers.append((k, n)) # pt2: store length as well
            k += n
    else:
        if n > 0:
            block += ["."]*n 
            spaces.append((k, n))  
            k += n
    j+= 1

# move file blocks
while True:
    if not numbers:
        break 
    n = numbers.pop()  
    
    for j in range(len(spaces)):
        s = spaces[j]
        
        if s[1] >= n[1] and s[0] < n[0]: # file fits?
            block[s[0]: s[0]+n[1]] = block[n[0]: n[0]+n[1]]
            block[n[0]: n[0]+n[1]] = ["."]*n[1]
            if s[1] == n[1]:
                del spaces[j]
            else:
                spaces[j] = (s[0]+n[1], s[1]-n[1]) # remaining space
            spaces.append((n[0], n[1])) # new space is created 
            break 

s = 0 
for j, block_j in enumerate(block):
    if block_j != ".":
        s += j * int(block_j)
print(s)
