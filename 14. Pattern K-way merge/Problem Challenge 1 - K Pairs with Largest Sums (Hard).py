'''
Problem Challenge 1
K Pairs with Largest Sums (Hard) 
Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.

Example 1:

Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
Output: [9, 3], [9, 6], [8, 6] 
Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.

Example 2:

Input: L1=[5, 2, 1], L2=[2, -1], K=3
Output: [5, 2], [5, -1], [2, 2] 
'''


#mycode
from heapq import * 
def find_k_largest_pairs(nums1, nums2, k):
  result = []
  # TODO: Write your code here
  heap = []
  
  for i in range(min(k, len(nums1))):
    for j in range(min(k, len(nums2))):
      if len(heap) < k:
        heappush(heap,(nums1[i]+nums2[j],[nums1[i],nums2[j]]))
      else:
        if nums1[i]+nums2[j] > heap[0][0]:
          heappop(heap)
          heappush(heap,(nums1[i]+nums2[j],[nums1[i], nums2[j]]))
  
  while heap:
    _, ans = heappop(heap)
    result.append(ans)

  return result


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()




#answer
from __future__ import print_function
from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
  minHeap = []
  for i in range(0, min(k, len(nums1))):
    for j in range(min(k, len(nums2))):
      if len(minHeap) < k:
        heappush(minHeap, (nums1[i] + nums2[j], i, j))
      else:
        # if the sum of the two numbers from the two arrays is smaller than the smallest(top)
        # element of the heap, we can 'break' here. Since the arrays are sorted in the
        # descending order, we'll not be able to find a pair with a higher sum moving forward
        if nums1[i] + nums2[j] < minHeap[0][0]:
          break
        else:  # we have a pair with a larger sum, remove top and insert this pair in the heap
          heappop(minHeap)
          heappush(minHeap, (nums1[i] + nums2[j], i, j))

  result = []
  for (num, i, j) in minHeap:
    result.append([nums1[i], nums2[j]])

  return result


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()





'''
Time complexity 
Since, at most, we’ll be going through all the elements of both arrays and we will add/remove one element in the heap in each step, 
the time complexity of the above algorithm will be O(N*M*logK) where ‘N’ and ‘M’ are the total number of elements in both arrays, respectively.

If we assume that both arrays have at least ‘K’ elements then the time complexity can be simplified to O(K^2logK), 
because we are not iterating more than ‘K’ elements in both arrays.

Space complexity 
The space complexity will be O(K) because, at any time, our Min Heap will be storing ‘K’ largest pairs.
'''