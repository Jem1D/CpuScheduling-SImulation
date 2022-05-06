def swap(a,b):
    temp2=pid[a]
    pid[a]=pid[b]
    pid[b]=temp2

    temp = arr[a]
    arr[a]=arr[b]
    arr[b]=temp

    temp1 = bur[a]
    bur[a]=bur[b]
    bur[b]=temp1

    temp1 = prio[a]
    prio[a]=prio[b]
    prio[b]=temp1

print("Enter number of processes:")
n = int(input())
arr =[]
bur=[]
pid=[]
prio=[]
total_turn=0
total_wait=0
# Taking arrival and burst time for each process
for i in range(n):
    print("Enter the arrival time, burstTime and priority of operation {}".format(i))
    a,b,c = map(int,input().split())
    arr.append(a)
    bur.append(b)
    prio.append(c)
    pid.append(i)

# Finding the first process to arrive as it will always execute first.
m = arr[0]
m_ind=0
for i in range(n):
    if(arr[i]<m):
        m=arr[i]
        m_ind=i
swap(0,m_ind)

#Sorting according to the arrival time.
for i in range(1,n):
    for j in range(i+1,n):
        if(prio[j]<prio[i]):
            swap(j,i)

sum=0
comp=[]
turn=[]
wait=[]
serv=[]

# Calculating completion, waiting and turnAround time for each process.

for i in range(n):
    serv.append(sum)
    a=arr[i]
    if(i==0):
        if(arr[i]>0):
            sum+=bur[i]+arr[i]
        else:
            sum+=bur[i]
    else:
        if(arr[i]>comp[i-1]):
            sum+=bur[i]+arr[i]-comp[i-1]
        else:
            sum+=bur[i]
    
    turn.append(sum-arr[i])
    total_turn+=turn[i]

    wait.append(turn[i]-bur[i])
    total_wait+=wait[i]

    comp.append(sum)
    
print(end='\n')

# forming table for tabular presentation.
d=[]
for i in range(n):
    a=[]
    a.append(pid[i])
    a.append(arr[i])
    a.append(bur[i])
    a.append(prio[i])
    a.append(comp[i])
    a.append(turn[i])
    a.append(wait[i])
    d.append(a)
print(end="\n")
print ("{:<6} {:<8} {:<8} {:<9} {:<10} {:<12} {:<12}".format('PID','Arrival','Burst','Priority','Completion','TurnAround','Wait'))

for v in d:
    pid,a,b,p,com,turn,wait= v
    print ("{:<6} {:<8} {:<8} {:<9} {:<10} {:<12} {:<12}".format( pid,a, b,p,com,turn,wait))
print(end='\n')

print("Average waiting time: {}".format(round(total_wait/n,2)),end='\n')
print("Average TurnAround time: {}".format(round(total_turn/n,2)),end='\n')
print(end='\n')

# Gantt chart
print("Gantt chart:",end='\n')
print("|",end='')

for i in range(n):
    if(i==0):
        if(arr[i]!=0):
            print(4*'/',end='')
            print('|',end='')
    else:
        s = bur[i]+comp[i-1]
        if(comp[i]>s):
            print(4*'/',end='')
            print('|',end='')
            
    print(4*"_",end='')
    print("|",end='')
print(end='\n')


for i in range(n):
    print(serv[i],end='')
    print(4*' ',end='')
    if(i==0):
        if(arr[i]!=0):
            print(arr[i],end='')
            print(4*' ',end='')
    elif(arr[i]>comp[i-1]):
        print(arr[i],end='')
        print(4*' ',end='')
print(sum,end='\n')