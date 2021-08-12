'''
Problem Challenge 2
Find the Smallest Missing Positive Number (medium)

Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'

Example 2:

Input: [3, -2, 0, 1, 2]
Output: 4

Example 3:

Input: [3, 2, 5, 1]
Output: 4
'''

#mycode
def find_first_missing_positive(nums):
  # TODO: Write your code here
  i=0
  while i < len(nums):
    j=nums[i]-1
    if j >= 0 and j < len(nums):
      if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
      else:
        i+=1
    else:
      i+=1
    
  for i in range(len(nums)):
    if nums[i]-1 != i:
      return i+1


#answer
def find_first_missing_positive(nums):
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  for i in range(n):
    if nums[i] != i + 1:
      return i + 1

  return nums.length + 1


def main():
  print(find_first_missing_positive([-3, 1, 5, 4, 2]))
  print(find_first_missing_positive([3, -2, 0, 1, 2]))
  print(find_first_missing_positive([3, 2, 5, 1]))


main()


'''
Time complexity 
The time complexity of the above algorithm is O(n).

Space complexity 
The algorithm runs in constant space O(1).
'''