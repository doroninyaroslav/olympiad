n=int(input())
mas=[0]*n
h=24
t=60
t2=0
for i in range(n):
    k=[int(g) for g in input().split()]
    mas[i]=k
for i in mas:
    while True:
        t2+=1
        i[1]+=1
        if i[1]==60:
            i[1]=0
            i[0]+=1
        if i[0]==24 and i[1]==0:
            break
    print(t2)
    t2=0
        
        

        

    

    
