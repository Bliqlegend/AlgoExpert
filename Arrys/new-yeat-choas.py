def minimumBribes(q):
    count = 0
    for i in range(len(q)):
        counter = 0
        for j in range(i+1,len(q)):
            if q[j] < q[i]:
                count+=1
                counter+=1
                if counter>2:return 'Too chaotic'  
    return count

q = [5 ,1 ,2 ,3 ,7 ,8 ,6, 4]
v = minimumBribes(q)
print(v)