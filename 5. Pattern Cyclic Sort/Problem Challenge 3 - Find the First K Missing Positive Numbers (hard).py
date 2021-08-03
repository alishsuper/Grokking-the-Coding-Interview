'''
Problem Challenge 3

Find the First K Missing Positive Numbers (hard)

Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Example 1:

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.

Example 2:

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.

Example 3:

Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
'''

#mycode
def find_first_k_missing_positive(nums, k):
  missingNumbers = []
  # TODO: Write your code here
  i=0
  while i < len(nums):
    j=nums[i]-1
    if j >= 0 and j<len(nums) and nums[i] != nums[j]:
      nums[i], nums[j]=nums[j], nums[i]
    else:
      i += 1
  
  i=0
  while i < len(nums) :
    if nums[i]-1 != i:
      missingNumbers.append(i+1)
    i+=1
  
  i=1
  if k <= len(missingNumbers):
    missingNumbers = missingNumbers[:k]
  else:
    while len(missingNumbers) < k:
      if max(missingNumbers)+1 < max(nums) and max(missingNumbers)+1 not in nums:
        missingNumbers.append(max(missingNumbers)+1)
      else:
        missingNumbers.append(max(nums)+i)
        i += 1

  return missingNumbers


#answer

def find_first_k_missing_positive(nums, k):
  n = len(nums)
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  missingNumbers = []
  extraNumbers = set()
  for i in range(n):
    if len(missingNumbers) < k:
      if nums[i] != i + 1:
        missingNumbers.append(i + 1)
        extraNumbers.add(nums[i])

  # add the remaining missing numbers
  i = 1
  while len(missingNumbers) < k:
    candidateNumber = i + n
    # ignore if the array contains the candidate number
    if candidateNumber not in extraNumbers:
      missingNumbers.append(candidateNumber)
    i += 1

  return missingNumbers


def main():
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))


main()


'''
Time complexity 
The time complexity of the above algorithm is O(n + k), as the last two for loops will run for O(n) and O(k) times respectively.

Space complexity 
The algorithm needs O(k) space to store the extraNumbers.
'''