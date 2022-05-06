# def merge(arr, l,  m,  r):

#     n1 = m - l + 1
#     n2 = r - m
#     L=[] 
#     R=[]

#     for i in range(n1):
#         L.append(arr[l + i])
#     for j in range(n2):
#         R.append(arr[m + 1 + j])

#     i = 0
#     j = 0
#     k = l
#     while (i < n1 and j < n2):
#         if (L[i] <= R[j]):
#             arr[k] = L[i]
#             i+=1
#         else:
#             arr[k] = R[j]
#             j+=1
        
#         k+=1
    
#     while (i < n1):
#         arr[k] = L[i]
#         i+=1
#         k+=1
    
#     while (j < n2):
#         arr[k] = R[j]
#         j+=1
#         k+=1
    

  
# def mergeSort(arr, l,  r):

#     if (l < r) :
#         m = l + (r - l) / 2
#         mergeSort(arr, l, m)
#         mergeSort(arr, m + 1, r)
#         merge(arr, l, m, r)
    


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

#taking the input for number of processes:
print("Enter number of processes:")
n = int(input())
arr =[]
bur=[]
pid=[]
total_turn=0
total_wait=0

# Taking arrival and burst time for each process
for i in range(n):
    print("Enter the arrival time and burst time of operation {}".format(i))
    a,b = map(int,input().split())
    arr.append(a) # adding to the arrays : Arrival, Burst and Process ID
    bur.append(b)
    pid.append(i)

#Sorting according to the arrival time
for i in range(n):
    for j in range(i+1,n):
        if(arr[j]<arr[i]):
            swap(j,i)
        elif(arr[j]==arr[i] and pid[j]<pid[i]):
            swap(j,i)

currT=0
comp=[]
turn=[]
wait=[]
serv=[]
alloted=[]

# Calculating completion, waiting and turnAround time for each process.

for i in range(n):
    serv.append(currT)
    a=arr[i]
    if(i==0): #Condition for first process
        if(arr[i]>0): #If the arrival of first is greater than 0, then its completion will be arrival + Burst
            currT+=bur[i]+arr[i]
        else:
            currT+=bur[i] #Else completion will be the burst time
        alloted.append(arr[i]) #CPU will be alloted to process 1 at arrival of 1st process
    else:
        if(arr[i]>comp[i-1]): #if the arrival of current process is greater than the completion of previous process
            currT+=bur[i]+arr[i]-comp[i-1] #then its completion will be the addition of the gap and its burst time.
            alloted.append(arr[i]) #CPU allocation will be arrival time of the process

        else:  #if the arrival of current process is less than or equal to the completion of previous process
            currT+=bur[i] #then the completion will current time + Burst time.
            alloted.append(comp[i-1]) #CPU allocation will the completion of previous process
    
    turn.append(currT-arr[i]) # Turn arround will be current time - its arrival time.
    total_turn+=turn[i] # adding turnAround of each process for the average calculation.

    wait.append(turn[i]-bur[i]) # Waiting time be turnAround - Burst Time.
    total_wait+=wait[i] # adding waiting of each process for the average calculation.

    comp.append(currT)
    
print(end='\n')

#Visual presentation:

# forming table for tabular presentation.
d=[]
for i in range(n):
    a=[]
    a.append(pid[i])
    a.append(arr[i])
    a.append(bur[i])
    a.append(comp[i])
    a.append(turn[i])
    a.append(wait[i])
    a.append(alloted[i])
    d.append(a)
print(end="\n")
print ("{:<6} {:<8} {:<8} {:<10} {:<10} {:<10} {:<10}".format('PID','Arrival','Burst','Completion','TurnAround','Wait','Allotment'))

for v in d:
    ppid,a,b,com ,turn,wait,all= v
    print ("{:<6} {:<8} {:<8} {:<10} {:<10} {:<10} {:<10}".format( ppid,a, b, com,turn,wait,all))
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
            
    print(2*"_",pid[i],2*'_',sep='',end='')
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
print(currT,end='\n')