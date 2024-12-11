
input = "27 10647 103 9 0 5524 4594227 902936"

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

class Stone:
    # define stones and how they are processed
    memory = {}

    def __init__(self,x0):
        self.history = [x0]
        self.x = x0
        self.__class__.memory[x0] = self

    def __repr__(self):
        return "<%s>" % self.history 
    
    def process(self, n_steps):
        k = 0
        while k < n_steps:
            new_stones = transform(self.x)
            if len(new_stones) == 2: # has reached splitting point 
                self.history.append(new_stones)
                for n in new_stones:
                    if (n not in self.__class__.memory):
                        Stone(n).process(n_steps)
                break 
            elif len(new_stones) == 1: # not yet splitting point reached
                self.history.append(new_stones[0])
            self.x = new_stones[0]
            k+=1

n_blinks = 75 # define number of blinks

# pre process stone histories
stones = [Stone(li) for li in l]
for stone in stones:
    stone.process(n_blinks)

trace_memory = {}
def count_traces(x, n): # count traces at stone value x for n steps recursively
    if (x,n) in trace_memory:
        return trace_memory[(x,n)]
    m = Stone.memory[x].history
    if n >= len(m)-1:
        traces = 0 
        for s in m[-1]:
            traces += count_traces(s, n-len(m)+1)
        trace_memory[(x,n)] = traces 
        return traces
    return 1 

# compute total length of chain
s = 0
for stone_val in l:
   s += count_traces(stone_val, n_blinks)
print(s)