'''
Problem Statement 
Given an array with positive numbers and a target number, 
find all of its contiguous subarrays whose product is less than the target number.

Example 1:

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.
Example 2:

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
'''

#mycode
def find_subarrays(arr, target):
  result = []
  product = 1
  win_start=0

  for win_end in range(len(arr)):

    product *= arr[win_end]
    print(product)
    
    while product >= target and win_start < len(arr):
      product /= arr[win_start]
      win_start += 1
    
    if product < target:
      temp_i=[]
      for i in range(win_end, win_start-1,-1):
        temp_i.append(arr[i])     
        temp=temp_i.copy()
        result.append(temp)

  return result



#answer
from collections import deque


def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    product *= arr[right]
    while (product >= target and left < len(arr)):
      product /= arr[left]
      left += 1
    # since the product of all numbers from left to right is less than the target therefore,
    # all subarrays from lef to right will have a product less than the target too; to avoid
    # duplicates, we will start with a subarray containing only arr[right] and then extend it
    temp_list = deque()
    for i in range(right, left-1, -1):
      temp_list.appendleft(arr[i])
      result.append(list(temp_list))
  return result


def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()


'''
Time complexity 
The main for-loop managing the sliding window takes O(N)but creating subarrays can take up to O(N^2) in the worst case. 
Therefore overall, our algorithm will take O(N^3).

Space complexity 
Ignoring the space required for the output list, the algorithm runs in O(N) space which is used for the temp list.
At the most, we need a space of O(n^2) for all the output lists.
'''