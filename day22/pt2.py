from itertools import cycle
import sys 

def mix(x, y): return x^y 
def prune(x): return x % 16777216

ops = cycle([lambda x: prune(mix(x, x*64)), lambda x: prune(mix(x, int(x/32))), lambda x: prune(mix(x, x*2048))])

def update(sn):
    for _ in range(3):
        op = next(ops)
        sn = op(sn)
    return sn

input = list(map(int, open("input.txt", "r").readlines()))
# input = [1,2,3,2024]

scores = {} # stores sequence -> score for each secret number 

N = 2000
M = len(input)
for i in range(M):
    n = input[i]
    num = []
    price = []
    chg = []
    sys.stdout.write(f"Progress: {100*i/M:.2f}%\r")
    for _ in range(N):
        last = n 
        n = update(n)
        num.append(n)
        price.append(int(str(n)[-1]))
        chg.append(int(str(n)[-1])-int(str(last)[-1]))
    
    breaks = set() # brakepoints: once traded, we cannot trade again
    for j in range(3, N):
        seq = tuple(chg[j-3:j+1])
        if seq in breaks: continue 
        breaks.add(seq)
        if seq not in scores:
            scores[seq] = []
        scores[seq].append(price[j])

# print(scores[(-2,1,-1,3)])
print("\n", max([sum(v) for v in scores.values()])) # determine max. score 
