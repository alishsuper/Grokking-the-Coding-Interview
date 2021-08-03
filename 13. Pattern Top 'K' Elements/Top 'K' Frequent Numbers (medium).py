'''
Problem Statement 
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
'''

#mycode
from heapq import *

def find_k_frequent_numbers(nums, k):
  topNumbers = []
  result = []
  # TODO: Write your code here
  mapping = {}
  for num in nums:
    if num not in mapping:
      mapping[num] = 1
    else:
      mapping[num] += 1
  
  for num, freq in mapping.items():
    if len(result)<k:
      heappush(result,(freq, num))
    else:
      if freq > result[0][0]:
        heappop(result)
        heappush(result,(freq, num))
  
  for i in range(len(result)-1,-1,-1):
    topNumbers.append(result[i][1])
  return topNumbers


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()



#answer
from heapq import *


def find_k_frequent_numbers(nums, k):

  # find the frequency of each number
  numFrequencyMap = {}
  for num in nums:
    numFrequencyMap[num] = numFrequencyMap.get(num, 0) + 1

  minHeap = []

  # go through all numbers of the numFrequencyMap and push them in the minHeap, which will have
  # top k frequent numbers. If the heap size is more than k, we remove the smallest(top) number
  for num, frequency in numFrequencyMap.items():
    heappush(minHeap, (frequency, num))
    if len(minHeap) > k:
      heappop(minHeap)

  # create a list of top k numbers
  topNumbers = []
  while minHeap:
    topNumbers.append(heappop(minHeap)[1])

  return topNumbers


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()



'''
Time complexity 
The time complexity of the above algorithm is O(N+N*logK).

Space complexity 
The space complexity will be O(N). Even though we are storing only ‘K’ numbers in the heap. 
For the frequency map, however, we need to store all the ‘N’ numbers.
'''