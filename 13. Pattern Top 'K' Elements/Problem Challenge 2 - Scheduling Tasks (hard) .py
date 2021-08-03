'''
Problem Challenge 2
Scheduling Tasks (hard) 

You are given a list of tasks that need to be run, in any order, on a server. Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

If at any time the server can’t execute any task then it must stay idle.

Example 1:

Input: [a, a, a, b, c, c], K=2
Output: 7
Explanation: a -> c -> b -> a -> c -> idle -> a

Example 2:

Input: [a, b, a], K=3
Output: 5
Explanation: a -> b -> idle -> idle -> a
'''

#mycode
from heapq import *
from collections import deque

def schedule_tasks(tasks, k):
  intervalCount = 0
  # TODO: Write your code here
  mapping = {}
  for i in tasks:
    mapping[i] = mapping.get(i,0) + 1
  
  heap = []
  for i, freq in mapping.items():
    heappush(heap,(-freq,i))
  
  queue = deque()
  char = ''
  while heap:
      freq, i = heappop(heap)
      
      intervalCount += 1
      if i == char:
        print(k-len_queue)
        intervalCount += (k-len_queue)
      queue.append((freq,i))
      
      
      
      if len(queue) > k:
        freq, i = queue.popleft()
        if -freq > 1:
          char = i
          heappush(heap,(freq+1,i))
      
      if heap == [] and queue != []:
        freq, i = queue.popleft()
        if -freq > 1:
          char = i
          heappush(heap,(freq+1,i))
      
      len_queue = len(queue) 

  return intervalCount


def main():
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))


main()



#answer
from heapq import *


def schedule_tasks(tasks, k):
  intervalCount = 0
  taskFrequencyMap = {}
  for char in tasks:
    taskFrequencyMap[char] = taskFrequencyMap.get(char, 0) + 1

  maxHeap = []
  # add all tasks to the max heap
  for char, frequency in taskFrequencyMap.items():
    heappush(maxHeap, (-frequency, char))

  while maxHeap:
    waitList = []
    n = k + 1  # try to execute as many as 'k+1' tasks from the max-heap
    while n > 0 and maxHeap:
      intervalCount += 1
      frequency, char = heappop(maxHeap)
      if -frequency > 1:
        # decrement the frequency and add to the waitList
        waitList.append((frequency+1, char))
      n -= 1

    # put all the waiting list back on the heap
    for frequency, char in waitList:
      heappush(maxHeap, (frequency, char))

    if maxHeap:
      intervalCount += n  # we'll be having 'n' idle intervals for the next iteration

  return intervalCount


def main():
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))


main()



'''

Time complexity 
The time complexity of the above algorithm is O(N*logN) where ‘N’ is the number of tasks. 
Our while loop will iterate once for each occurrence of the task in the input (i.e. ‘N’) and 
in each iteration we will remove a task from the heap which will take O(logN) time. 
Hence the overall time complexity of our algorithm is O(N*logN).

Space complexity 
The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ tasks in the HashMap.
'''