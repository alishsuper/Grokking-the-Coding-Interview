'''
Problem Statement 
Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. 
The cost of connecting two ropes is equal to the sum of their lengths.

Example 1:

Input: [1, 3, 11, 5]
Output: 33
Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)
Example 2:

Input: [3, 4, 5, 6]
Output: 36
Explanation: First connect 3+4(=7), then 5+6(=11), 7+11(=18). Total cost is 36 (7+11+18)
Example 3:

Input: [1, 3, 11, 5, 2]
Output: 42
Explanation: First connect 1+2(=3), then 3+3(=6), 6+5(=11), 11+11(=22). Total cost is 42 (3+6+11+22)
'''


#mycode
from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):
  result = []
  # TODO: Write your code here
  for i in ropeLengths:
    heappush(result,i)
  
  lenghth = 0
  while len(result)>1:
    temp = heappop(result) + heappop(result)
    lenghth += temp
    heappush(result,temp)
  return lenghth


def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()



#answer
from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
  minHeap = []
  # add all ropes to the min heap
  for i in ropeLengths:
    heappush(minHeap, i)

  # go through the values of the heap, in each step take top (lowest) rope lengths from the min heap
  # connect them and push the result back to the min heap.
  # keep doing this until the heap is left with only one rope
  result, temp = 0, 0
  while len(minHeap) > 1:
    temp = heappop(minHeap) + heappop(minHeap)
    result += temp
    heappush(minHeap, temp)

  return result


def main():

  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))

main()




'''
Time complexity 
Given ‘N’ ropes, we need O(N*logN)to insert all the ropes in the heap. 
In each step, while processing the heap, we take out two elements from the heap and insert one. 
This means we will have a total of ‘N’ steps, having a total time complexity of O(N*logN).

Space complexity #
The space complexity will be O(N) because we need to store all the ropes in the heap.
'''