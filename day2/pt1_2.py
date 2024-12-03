input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""" # ... insert input here 

def check_order(items, op, t=0):
    n = len(items)
    for k in range(n-1):
        if not op(items[n-k-1], items[n-k-2]):
            return 0, t
    return 1, t

def check_line(items, t=0):
    asc = lambda x,y: x>=y and 1<=abs(x-y)<=3 
    des = lambda x,y: x<=y and 1<=abs(x-y)<=3 
    
    def check_safe(items):
        x, _ = check_order(items[:], asc)
        if x> 0: return True 
        y, _ = check_order(items[:], des)
        if y > 0: return True 
        return False 
    
    # part 1 
    if check_safe(items):
        return 1 
    
    # part 2
    # for k in range(len(items)): 
    #     # try to fix sequence by removing one level
    #     # NOTE slow but works
    #     new_items = items[:]
    #     del new_items[k]
    #     if check_safe(new_items): return 1 
    
    return 0

s = 0
for line in input.split("\n"):
    items = list(map(int, line.split()))
    s += check_line(items)

print(s)