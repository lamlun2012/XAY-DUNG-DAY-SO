with open("SEQUENCE.INP", "r") as f:
    n = int(f.readline())
    commands = [tuple(map(int, f.readline().split())) for _ in range(n)]

seq = [commands[0][1]]

for i in range(1, n):
    x, y = commands[i]
    seq.insert(x - 1, y)  

with open("SEQUENCE.OUT", "w") as f:
    f.write(" ".join(map(str, seq)))
