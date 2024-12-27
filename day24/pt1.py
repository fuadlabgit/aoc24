
import heapq 

input = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""

input = open("input.txt", "r").read()

ops = {"AND": lambda x, y: 1 if (x==1 and y==1) else 0,
       "XOR": lambda x, y: 1 if x!=y else 0,
       "OR": lambda x, y:  1 if (x==1 or y == 1) else 0
       } 

avail = {}
for line in input.split("\n\n")[0].splitlines():
    j = line.split(": ")
    avail[j[0]] = int(j[1])

gates = {}
for line in input.split("\n\n")[1].splitlines():
    j = line.split(" -> ")
    gates[j[1].strip()] = tuple(j[0].split(" ")) # 0,0 indicates none of the inputs have been computed

def process(out_gate):
    if out_gate in avail: return True 
    x = gates[out_gate]
    op = ops[x[1]]
    in_gates = (x[0], x[2])
    if in_gates[0] in avail and in_gates[1] in avail:
       avail[out_gate] = op(avail[in_gates[0]], avail[in_gates[1]])
       return True 
    return False

q = [(0,k) for k in gates.keys()]
k = 0
while q: 
    prio, nxt = heapq.heappop(q)
    success = process(nxt)
    if not success: heapq.heappush(q, (k, nxt))
    k += 1 

z_wires = sorted(list([k for k in gates.keys() if k.startswith("z")])) 

sol = {z:avail[z] for z in z_wires}
sol_binary = "".join([str(sol[z]) for z in z_wires[::-1]])
print(int(sol_binary,2))
