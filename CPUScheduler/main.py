# Question 4 FIFO

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
# 2GHz Processors
slower_processor_upper_bound = 3
slower_processor_lower_bound = 1
# 4GHz Processors
faster_processor_upper_bound = 6
faster_processor_lower_bound = 4

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
  memory = customMemoryDistribution(memory_upper_bound, memory_lower_bound)
  # Converting burst times to cycles/second from milliseconds
  burst_time[i] = burst_time[i]//1000 
  
  # If burst time is less than or equal to 2 billion cycles/s
  # and less than 8GB are required, process is assigned 
  # to one of the 8GB 2GHz processors (P1-P3)
  if burst_time[i] <= 2*10**9 and memory <= 80000:
    processors = customProcessor(slower_processor_upper_bound, slower_processor_lower_bound)
    
  # All processes requiring over 8GB are assigned to the 
  # 16GB 4GHz processors (P4-P6) regardless of burst time
  else:
      processors = customProcessor(faster_processor_upper_bound, faster_processor_lower_bound)
    
  
  #memory = customMemoryDistribution(memory_upper_bound, memory_lower_bound)
  
  findWaitingTime(number_of_processes, waiting_time, burst_time)
  findTurnAroundTime(number_of_processes, waiting_time, burst_time, turnaround_time)
  process = [i + 1, processors, memory, waiting_time[i], burst_time[i],       turnaround_time[i]]
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