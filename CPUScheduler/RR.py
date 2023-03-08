# Question 1 Round Robin

import csv
import random

# Memory requirement in between [1MB - 16GB]
def customMemoryDistribution (upper_bound, lower_bound):
  value = int(random.gauss(upper_bound, lower_bound))
  result = value % (upper_bound - lower_bound + 1) + lower_bound
  return result

# Function to create processors
def customProcessor(upper_bound, lower_bound):
  value = int(random.gauss(upper_bound, lower_bound))
  result = value % (upper_bound - lower_bound + 1) + lower_bound
  return result

# Function to calculate turn around time
def findTurnAroundTime(number_of_processes, wt, bt, tat):
    for i in range(number_of_processes):
        tat[i] = bt[i] + wt[i]

# Function to calculate waiting time
def findWaitingTime(number_of_processes, wt, bt, quantum):
    rem_bt = [0] * number_of_processes # Remaining burst time
 
    for i in range(number_of_processes):
        rem_bt[i] = bt[i]
    t = 0 # Current time
  
    # Traversing processes in round
    # robin manner until all have executed
    while(1):
        done = True
        for i in range(number_of_processes):
             
            # If burst time of a process is greater
            # than 0, then there are pending processes
            if (rem_bt[i] > 0) :
                done = False 

                # If burst time is greater than time slice,
                # then current time must increase by time slice
                if (rem_bt[i] > quantum) :
                    t += quantum
                    rem_bt[i] -= quantum
                 
                # If burst time is less than or equal 
                # to time slice, establish final cycle
                else:             
                    t = t + rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
                
        if (done == True):
          break

# Parameter Declarations
number_of_processes = 250

# Processors
processor_upper_bound = 6
processor_lower_bound = 1

# Memory of processes in KB
memory_upper_bound = 16000000
memory_lower_bound = 1000

# Burst Time
bt = [random.randrange(10*10**6, 10*10**12) for i in range(number_of_processes)]

wt = [0] * number_of_processes
tat = [0] * number_of_processes

# Time slice (quantum) for each process
quantum = 10*10**12

process_list = []

# Loop that runs calculations for all 250 processes among 6 processors
for i in range(number_of_processes):
    processors = customProcessor(processor_upper_bound, processor_lower_bound)
    memory = customMemoryDistribution(memory_upper_bound, memory_lower_bound)
  
    findWaitingTime(number_of_processes, wt, bt, quantum)
    findTurnAroundTime(number_of_processes, wt, bt, tat)
    process = [i + 1, processors, memory, wt[i], bt[i], tat[i]]
    process_list.append(process)

    total_waiting_time = 0
    total_turnaround_time = 0
    total_waiting_time = total_waiting_time + wt[i]
    total_turnaround_time = total_turnaround_time + tat[i]
  

    
# Open or Create File to Write Data
with open('processes.csv', 'w', newline='') as csvfile:
    # Initialize Writer Class
    writer = csv.writer(csvfile)
    # Write Column Headers
    writer.writerow(['Process ID:' ' Processor:' ' Memory Requirement:' ' Waiting Time:' ' Burst Time:' ' Turn Around Time:   '])
    # Write Process Data
    writer.writerows(process_list)
  
print('Average waiting time = ' + str(total_waiting_time / number_of_processes))
print('Average turn around time = ' + str(total_turnaround_time / number_of_processes))