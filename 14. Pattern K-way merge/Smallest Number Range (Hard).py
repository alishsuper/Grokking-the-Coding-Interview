'''
Problem Statement 
Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

Example 1:

Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.
Example 2:

Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
Output: [9, 12]
Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3.
'''


#mycode
from heapq import *
import math

def find_smallest_range(lists):
  # TODO: Write your code here
  heap = []
  start, end = -math.inf, math.inf
  current_max = -math.inf
  for i in lists:
    heappush(heap,(i[0],0,i))
    current_max = max(i[0], current_max)
  
  while len(heap) == len(lists):
    number, i, current_list = heappop(heap)

    if current_max - number < end - start:
      start = number
      end = current_max
    
    if i+1 < len(current_list):
      heappush(heap,(current_list[i+1],i+1,current_list))
      current_max = max(current_max,current_list[i+1])

  return [start, end]


def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()



#answer
from heapq import *
import math


def find_smallest_range(lists):
  minHeap = []
  rangeStart, rangeEnd = 0, math.inf
  currentMaxNumber = -math.inf

  # put the 1st element of each array in the max heap
  for arr in lists:
    heappush(minHeap, (arr[0], 0, arr))
    currentMaxNumber = max(currentMaxNumber, arr[0])

  # take the smallest(top) element form the min heap, if it gives us smaller range, update the ranges
  # if the array of the top element has more elements, insert the next element in the heap
  while len(minHeap) == len(lists):
    num, i, arr = heappop(minHeap)
    if rangeEnd - rangeStart > currentMaxNumber - num:
      rangeStart = num
      rangeEnd = currentMaxNumber

    if len(arr) > i+1:
      # insert the next element in the heap
      heappush(minHeap, (arr[i+1], i+1, arr))
      currentMaxNumber = max(currentMaxNumber, arr[i+1])

  return [rangeStart, rangeEnd]


def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()




'''
Time complexity 
Since, at most, we’ll be going through all the elements of all the arrays and will remove/add one element in the heap in each step, t
he time complexity of the above algorithm will be O(N*logM) where ‘N’ is the total number of elements in all the ‘M’ input arrays.

Space complexity 
The space complexity will be O(M) because, at any time, our min-heap will be store one number from all the ‘M’ input arrays.
'''