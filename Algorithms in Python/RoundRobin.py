
def swap(a,b):
    temp2=pid[a]
    pid[a]=pid[b]
    pid[b]=temp2

    temp = arrival[a]
    arrival[a]=arrival[b]
    arrival[b]=temp

    temp1 = burst[a]
    burst[a]=burst[b]
    burst[b]=temp1
    

print("Enter number of processes:")
n = int(input())
arrival =[]
burst=[]
pid=[]
total_turn=0
total_wait=0
# Taking arrival and burst time for each process
print("Enter the quanta for round robin: ")
quanta = int(input())
for i in range(n):
    print("Enter the arrival time and burst time of operation {}".format(i))
    a,b = map(int,input().split())
    arrival.append(a)
    burst.append(b)
    pid.append(i)

#Sorting according to the arrival time
for i in range(n):
    for j in range(i+1,n):
        if(arrival[j]<arrival[i]):
            swap(j,i)
        elif(arrival[j]==arrival[i] and pid[j]<pid[i]):
            swap(j,i)



class sjfzz:
    def __init__(self,_pid,_arrival,_burst):
        self.pid= _pid
        self.arrival= _arrival
        self.burst =  _burst




burst_copy = burst.copy()
m = max(burst)
if(m%quanta == 0):
    no_of_times = int(m/quanta)
else:
    no_of_times = int(m/quanta) + 1

timeline = []
sum=0
comp=[]
index = []
length = 0
turn=[]
wait=[]
serv=[]

pr_seq = []
currT = arrival[0]
timeline.append(currT)
for j in range(no_of_times):
    for i in range(n):
        if(burst_copy[i] >= quanta):
            currT += quanta
            timeline.append(currT)
            burst_copy[i] -= quanta
            pr_seq.append(pid[i])
        elif(burst_copy[i] !=0 and burst_copy[i] < quanta):
            currT += burst_copy[i]
            timeline.append(currT)
            burst_copy[i] = 0
            pr_seq.append(pid[i])
        if((burst_copy[i] == 0 and length==0) or (burst_copy[i]==0 and comp[length-1]!=currT)):
            index.append(i)
            comp.append(currT)
            length+=1
# comp_copy = comp.copy()
# comp = []
# print(*index)
# for i in range(n):
#     comp.append(comp_copy[index[i]])
for i in range(n):
    for j in range(i+1,n):
        if(index[j]<index[i]):
            temp = comp[i]
            comp[i] = comp[j]
            comp[j] = temp

            temp1 = index[i]
            index[i] = index[j]
            index[j] = temp1

# calculating turnAround and Waiting time
for i in range(n):
    turn.append(comp[i] - arrival[i])
    total_turn+=turn[i]
    wait.append(turn[i] - burst[i])
    total_wait+=wait[i]


print(*timeline)
# print(*comp)
print(*pr_seq)
#Sorting according to the burst time of available processes.
# next = 0
# abc = []
# completed = [] # Processes completed in order of increasing burst time and arrival time.
# currentTime = arrival[0]
# for j in range(n):

#     minTIme = 999
#     arrived = [] #Processes arrived in the queue
#     willComplete = currentTime+burst[next]

#     abc.append(sjfzz(pid[next],arrival[next],burst[next]))
#     completed.append(next)
#     currentTime+= burst[next]

#     for i in range(n):
#         if(arrival[i] <= willComplete):
#             arrived.append(i)

#     for i in completed:
#         if(i in arrived):
#             arrived.remove(i)

#     if(len(arrived)!=0):
#         for i in arrived:
#             if(burst[i] < minTIme):
#                 minTIme = burst[i]
#                 next = i
#     else:  # Condition when the arrived queue is empty
#         next +=1

# arrival =[]
# burst=[]
# pid=[]

# for i in abc: 
#     arrival.append(i.arrival)
#     burst.append(i.burst)
#     pid.append(i.pid)



# # Calculating completion, waiting and turnAround time for each process.
# sum=0
# comp=[]
# turn=[]
# wait=[]
# serv=[]

# for i in range(n):
#     serv.append(sum)
#     a=arrival[i]
#     if(i==0):
#         if(arrival[i]>0):
#             sum+=burst[i]+arrival[i]
#         else:
#             sum+=burst[i]
#     else:
#         if(arrival[i]>comp[i-1]):
#             sum+=burst[i]+arrival[i]-comp[i-1]
#         else:
#             sum+=burst[i]
    
#     turn.append(sum-arrival[i])
#     total_turn+=turn[i]

#     wait.append(turn[i]-burst[i])
#     total_wait+=wait[i]

#     comp.append(sum)
    
# # Below given code is for the representation purposes.

# forming table for tabular presentation.
d=[]
for i in range(n):
    a=[]
    a.append(pid[i])
    a.append(arrival[i])
    a.append(burst[i])
    a.append(comp[i])
    a.append(turn[i])
    a.append(wait[i])
    d.append(a)
print(end="\n")
print ("{:<6} {:<8} {:<8} {:<12} {:<12} {:<10}".format('PID','Arrival','Burst','Completion','TurnAround','Wait'))

for v in d:
    id,a,b,com ,t,w= v
    print ("{:<6} {:<8} {:<8} {:<12} {:<12} {:<10}".format( id,a, b, com,t,w))
print(end='\n')

print("Average waiting time: {}".format(round(total_wait/n,2)),end='\n')
print("Average TurnAround time: {}".format(round(total_turn/n,2)),end='\n')
print(end='\n')


# Gantt chart
# print("Gantt chart:",end='\n')
# print("|",end='')

# for i in range(n):
#     if(i==0):
#         if(arrival[i]!=0):
#             print(4*'/',end='')
#             print('|',end='')
#     else:
#         s = burst[i]+comp[i-1]
#         if(comp[i]>s):
#             print(4*'/',end='')
#             print('|',end='')
            
#     print(4*"_",end='')
#     print("|",end='')
# print(end='\n')


# for i in range(n):
#     print(serv[i],end='')
#     print(4*' ',end='')
#     if(i==0):
#         if(arrival[i]!=0):
#             print(arrival[i],end='')
#             print(4*' ',end='')
#     elif(arrival[i]>comp[i-1]):
#         print(arrival[i],end='')
#         print(4*' ',end='')
# print(sum,end='\n')