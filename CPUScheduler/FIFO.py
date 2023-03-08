# Question 1 FIFO

import csv
import random

# Memory requirement in between [1MB - 16GB]
def customMemoryDistribution (upper_bound, lower_bound):
  value = int(random.gauss(upper_bound, lower_bound))
  result = value % (upper_bound - lower_bound + 1) + lower_bound
  return result

# Range for processors in between 1 and 6
def customProcessor(upper_bound, lower_bound):
  value = int(random.gauss(upper_bound, lower_bound))
  result = value % (upper_bound - lower_bound + 1) + lower_bound
  return result

# Waiting Time function
def findWaitingTime(number_of_processes, waiting_time, burst_time):
    waiting_time[0] = 0
    for i in range (1, number_of_processes):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]

# Turn Around function
def findTurnAroundTime(number_of_processes, waiting_time, burst_time, turnaround_time):
    for i in range(number_of_processes):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

# Parameter Declarations
number_of_processes = 250

# Processors
processor_upper_bound = 6
processor_lower_bound = 1

# Memory of processes in KB
memory_upper_bound = 16000000
memory_lower_bound = 1000

# Burst Time
burst_time = [random.randrange(10*10**6, 10*10**12) for i in range(number_of_processes)]

waiting_time = [0] * number_of_processes
turnaround_time = [0] * number_of_processes

process_list = []

# loops through the algorithm 250 times
for i in range(number_of_processes):
    processors = customProcessor(processor_upper_bound, processor_lower_bound)
    memory = customMemoryDistribution(memory_upper_bound, memory_lower_bound)
  
    findWaitingTime(number_of_processes, waiting_time, burst_time)
    findTurnAroundTime(number_of_processes, waiting_time, burst_time, turnaround_time)
    process = [i + 1, processors, memory, waiting_time[i], burst_time[i], turnaround_time[i]]
    process_list.append(process)

    total_waiting_time = 0
    total_turnaround_time = 0
    total_waiting_time = total_waiting_time + waiting_time[i]
    total_turnaround_time = total_turnaround_time + turnaround_time[i]
    
# Open or Create File to Write Data
with open('processes.csv', 'w', newline='') as csvfile:
    # Initialize Writer Class
    writer = csv.writer(csvfile)

    # Write Column Headers
    writer.writerow(['Process ID:' ' Processor:' ' Memory Requirement:' ' Waiting Time:' ' Burst Time:' ' Turn Around Time:'])
    # Write Process Data
    writer.writerows(process_list)
    print('Average waiting time = ' + str(total_waiting_time / number_of_processes))
    print('Average turn around time = ' + str(total_turnaround_time / number_of_processes))