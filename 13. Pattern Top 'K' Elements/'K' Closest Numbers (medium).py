'''
Problem Statement 
Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. 
Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Example 1:

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]
Example 2:

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]
Example 3:

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]
'''

#mycode
from heapq import *

def find_closest_elements(arr, K, X):
  result = []
  
  # TODO: Write your code here
  temp1, temp2 = [], []
  for i in arr:
    heappush(temp1,(abs(X-i),i))

  i = K
  while i>0:
    heappush(temp2,heappop(temp1)[1])
    i -= 1

  while temp2:
    result.append(heappop(temp2))
  return result


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()




#answer
from heapq import *


def find_closest_elements(arr, K, X):
  index = binary_search(arr, X)
  low, high = index - K, index + K

  low = max(low, 0)  # 'low' should not be less than zero
  # 'high' should not be greater the size of the array
  high = min(high, len(arr) - 1)

  minHeap = []
  # add all candidate elements to the min heap, sorted by their absolute difference from 'X'
  for i in range(low, high+1):
    heappush(minHeap, (abs(arr[i] - X), arr[i]))

  # we need the top 'K' elements having smallest difference from 'X'
  result = []
  for _ in range(K):
    result.append(heappop(minHeap)[1])

  result.sort()
  return result


def binary_search(arr,  target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = int(low + (high - low) / 2)
    if arr[mid] == target:
      return mid
    if arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  if low > 0:
    return low - 1
  return low


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()


'''
Time complexity 
The time complexity of the above algorithm is O(logN + K*logK). 
We need O(logN) for Binary Search and O(K*logK) to insert the numbers in the Min Heap, 
as well as to sort the output array.

Space complexity 
The space complexity will be O(K), as we need to put a maximum of 2K2K numbers in the heap.
'''


'''
Alternate Solution using Two Pointers 
After finding the number closest to ‘X’ through Binary Search, 
we can use the Two Pointers approach to find the ‘K’ closest numbers. 
Let’s say the closest number is ‘Y’. 
We can have a left pointer to move back from ‘Y’ and a right pointer to move forward from ‘Y’. 
At any stage, whichever number pointed out by the left or the right pointer gives the smaller difference from ‘X’ 
will be added to our result list.

To keep the resultant list sorted we can use a Queue. 
So whenever we take the number pointed out by the left pointer, 
we will append it at the beginning of the list and whenever we take the number pointed out by the right pointer 
we will append it at the end of the list.

Here is what our algorithm will look like:
'''

from collections import deque


def find_closest_elements(arr, K, X):
  result = deque()
  index = binary_search(arr, X)
  leftPointer, rightPointer = index, index + 1
  n = len(arr)
  for i in range(K):
    if leftPointer >= 0 and rightPointer < n:
      diff1 = abs(X - arr[leftPointer])
      diff2 = abs(X - arr[rightPointer])
      if diff1 <= diff2:
        result.appendleft(arr[leftPointer])
        leftPointer -= 1
      else:
        result.append(arr[rightPointer])
        rightPointer += 1
    elif leftPointer >= 0:
      result.appendleft(arr[leftPointer])
      leftPointer -= 1
    elif rightPointer < n:
      result.append(arr[rightPointer])
      rightPointer += 1

  return result


def binary_search(arr,  target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = int(low + (high - low) / 2)
    if arr[mid] == target:
      return mid
    if arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  if low > 0:
    return low - 1
  return low


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()


'''
Time complexity 
The time complexity of the above algorithm is O(logN + K). 
We need O(logN) for Binary Search and O(K) for finding the ‘K’ closest numbers using the two pointers.

Space complexity 
If we ignoring the space required for the output list, the algorithm runs in constant space O(1).
'''