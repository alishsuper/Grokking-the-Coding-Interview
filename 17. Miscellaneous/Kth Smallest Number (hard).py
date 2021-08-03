'''
Problem Statement 
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Example 1:

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].
Example 2:

Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three smaller numbers are
[1, 2, 5].
Example 3:

Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
'''


#mycode
from heapq import *

def find_Kth_smallest_number(nums, k):
  # TODO: Write your code here
  heap = []
  for num in nums:
    if len(heap) < k:
      heappush(heap, -num)
    else:
      if -num > heap[0]:
        heappop(heap)
        heappush(heap, -num)
  return -heap[0]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()



#1. Brute-force
import math


def find_Kth_smallest_number(nums, k):
  # to handle duplicates, we will keep track of previous smallest number and its index
  previousSmallestNum, previousSmallestIndex = -math.inf, -1
  currentSmallestNum, currentSmallestIndex = math.inf, -1
  for i in range(k):
    for j in range(len(nums)):
      if nums[j] > previousSmallestNum and nums[j] < currentSmallestNum:
        # found the next smallest number
        currentSmallestNum = nums[j]
        currentSmallestIndex = j
      elif nums[j] == previousSmallestNum and j > previousSmallestIndex:
        # found a number which is equal to the previous smallest number; since numbers can repeat,
        # we will consider 'nums[j]' only if it has a different index than previous smallest
        currentSmallestNum = nums[j]
        currentSmallestIndex = j
        break  # break here as we have found our definitive next smallest number

    # current smallest number becomes previous smallest number for the next iteration
    previousSmallestNum = currentSmallestNum
    previousSmallestIndex = currentSmallestIndex
    currentSmallestNum = math.inf

  return previousSmallestNum


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()



'''
Time & Space Complexity 
The time complexity of the above algorithm will be O(N*K). The algorithm runs in constant space O(1).
'''



#2. Brute-force using Sorting
def find_Kth_smallest_number(nums, k):
  return sorted(nums)[k-1]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()



'''
Time & Space Complexity 
Sorting will take O(NlogN)O(NlogN) and if we are not using an in-place sorting algorithm, we will need O(N)O(N) space.
'''


#3. Using Max-Heap
from heapq import *


def find_Kth_smallest_number(nums, k):
  maxHeap = []
  # put first k numbers in the max heap
  for i in range(k):
    heappush(maxHeap, -nums[i])

  # go through the remaining numbers of the array, if the number from the array is smaller than the
  # top(biggest) number of the heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if -nums[i] > maxHeap[0]:
      heappop(maxHeap)
      heappush(maxHeap, -nums[i])

  # the root of the heap has the Kth smallest number
  return -maxHeap[0]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()



'''
Time & Space Complexity 
The time complexity of the above algorithm is O(K*logK + (N-K)*logK) which is asymptotically equal to O(N*logK). 
The space complexity will be O(K) because we need to store ‘K’ smallest numbers in the heap.
'''

'''
4. Using Min-Heap 
Also discussed in Kth Smallest Number, we can use a Min Heap to find the Kth smallest number. 
We can insert all the numbers in the min-heap and then extract the top ‘K’ numbers from the heap to find the Kth smallest number.

Time & Space Complexity 
Inserting all numbers in the heap will take O(N*logN) and extracting ‘K’ numbers will take O(K*logN). 
Overall, the time complexity of this algorithm will be O(N*logN+K*logN) and the space complexity will be O(N).
'''


#5. Using Partition Scheme of Quicksort 
def find_Kth_smallest_number(nums, k):
  return find_Kth_smallest_number_rec(nums, k, 0, len(nums) - 1)


def find_Kth_smallest_number_rec(nums, k, start, end):
  p = partition(nums, start, end)

  if p == k - 1:
    return nums[p]

  if p > k - 1:  # search lower part
    return find_Kth_smallest_number_rec(nums, k, start, p - 1)

  # search higher part
  return find_Kth_smallest_number_rec(nums, k, p + 1, end)


def partition(nums, low, high):
  if low == high:
    return low

  pivot = nums[high]
  for i in range(low, high):
    # all elements less than 'pivot' will be before the index 'low'
    if nums[i] < pivot:
      nums[low], nums[i] = nums[i], nums[low]
      low += 1

  # put the pivot in its correct place
  nums[low], nums[high] = nums[high], nums[low]
  return low


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
