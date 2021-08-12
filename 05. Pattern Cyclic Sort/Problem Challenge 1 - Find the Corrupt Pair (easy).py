'''
Problem Challenge 1

Find the Corrupt Pair (easy)

We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

Example 1:

Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.

Example 2:

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
'''


#mycode
def find_corrupt_numbers(nums):
  # TODO: Write your code here
  duplicate, missing = 0, 0
  i=0

  while i < len(nums):
    j=nums[i]-1
    if i != j:
      if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
      else:
        duplicate=nums[i]
        i += 1
    else:
      i += 1
    
  for i in range(len(nums)):
    if nums[i]-1 != i:
      missing= i+1
  return [duplicate, missing]


#answer
def find_corrupt_numbers(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  for i in range(len(nums)):
    if nums[i] != i + 1:
      return [nums[i], i + 1]

  return [-1, -1]


def main():
  print(find_corrupt_numbers([3, 1, 2, 5, 2]))
  print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()


'''
Time complexity 
The time complexity of the above algorithm is O(n).

Space complexity 
The algorithm runs in constant space O(1).
'''