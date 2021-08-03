'''
Problem Challenge 3

Minimum Window Sort (medium)

Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example 1:

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Example 2:

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

Example 3:

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted

Example 4:

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
'''


#mycode 
import math

def shortest_window_sort(arr):
  # TODO: Write your code here

  left, right = 1, len(arr) -1 
  max_num, min_num = -math.inf, math.inf

  while left < len(arr)-1  and arr[left] < arr[left+1]:
    left += 1
  
  while right > 0 and arr[right] > arr[right-1]:
    right -= 1
  
  for i in range(left, right+1):
    max_num = max(max_num, arr[i])
    min_num = min(min_num, arr[i])
  
  for i in range(left,-1,-1):
    if arr[i] >= min_num:
      left = i
  
  for i in range(right, len(arr)):
    if arr[i] <= max_num:
      right = i

  if right == 0:
    return 0

  return right-left+1



#answer
import math


def shortest_window_sort(arr):
  low, high = 0, len(arr) - 1
  # find the first number out of sorting order from the beginning
  while (low < len(arr) - 1 and arr[low] <= arr[low + 1]):
    low += 1

  if low == len(arr) - 1:  # if the array is sorted
    return 0

  # find the first number out of sorting order from the end
  while (high > 0 and arr[high] >= arr[high - 1]):
    high -= 1

  # find the maximum and minimum of the subarray
  subarray_max = -math.inf
  subarray_min = math.inf
  for k in range(low, high+1):
    subarray_max = max(subarray_max, arr[k])
    subarray_min = min(subarray_min, arr[k])

  # extend the subarray to include any number which is bigger than the minimum of the subarray
  while (low > 0 and arr[low-1] > subarray_min):
    low -= 1
  # extend the subarray to include any number which is smaller than the maximum of the subarray
  while (high < len(arr)-1 and arr[high+1] < subarray_max):
    high += 1

  return high - low + 1


def main():
  print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
  print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
  print(shortest_window_sort([1, 2, 3]))
  print(shortest_window_sort([3, 2, 1]))


main()

'''
Time complexity 
The time complexity of the above algorithm will be O(N)O(N).

Space complexity 
The algorithm runs in constant space O(1)O(1).
'''