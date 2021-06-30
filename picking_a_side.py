a =  [5, -2, 3 , 1, 2]
suma =[]
n = len(a)
middle = int(n/2)-1
npc = 3
for i in range(middle):
    if npc==0:
        break
    if a[i] > 0:   
        suma.append(a[i])
        npc-=1

for i in range(middle,len(a)):
    if npc==0:
        break
    if a[i] > 0:   
        suma.append(a[i])
        npc-=1

print(sum(suma))
    
        