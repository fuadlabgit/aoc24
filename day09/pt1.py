
dm = list("2333133121414131402") # disk map
# dm = list(open("input.txt", "r").read())

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
            for _ in range(n):
                numbers.append(k)   
                k += 1
    else:
        if n > 0:
            block += ["."]*n 
            for _ in range(n):
                spaces = [k] + spaces
                k += 1   
    j+= 1

# move file blocks
while True:

    i = spaces.pop()
    j = numbers.pop()  
    
    if i > j: # not numbers: # i > j or (not numbers) or (not spaces):
        break 
    
    block[i] = block[j]
    block[j] = "." 

    #print("".join(block))
    #print(" "*j+"^"+" "*(len(block)-j-1))
    #print(" "*i+"|"+" "*(len(block)-i-1))

numberblock = block[:j+1]
s = 0 
for j, block_j in enumerate(numberblock):
    s += j * int(block_j)
print(s)

