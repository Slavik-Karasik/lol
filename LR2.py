dt = 500
dn = [60, 200, 197, 150, 128, 72, 40, 30, 20, 20, 20, 20, 20, 20, 20, 30, 20, 10]
k = 18
N = []
l = []  

for i in range(k+1):
    N.append((sum(dn[i:]) + sum(dn[i+1:])) // 2)
    
for i in range(k):
    l.append(dn[i] / (dt * N[i]))

print('dt\tn(i)\tNср\tlambda')
for i in range(k):
    print(f'{dt*(i+1)}\t{dn[i]}\t{N[i]}\t{l[i]:.8f}')
