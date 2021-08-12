'''
Problem Statement 
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
'''

#mycode
def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
  i,j = 0, len(arr)-1
  while i < j:
    if arr[i]+arr[j] < target_sum:
      i+=1
    elif arr[i]+arr[j] > target_sum:
      j-=1
    else:
      return [i, j]
  
  return[-1,-1]


#answer
def pair_with_targetsum(arr, target_sum):
  left, right = 0, len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:
      return [left, right]

    if target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum
  return [-1, -1]


def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()



'''
Time Complexity 
The time complexity of the above algorithm will be O(N), 
where ‘N’ is the total number of elements in the given array.

Space Complexity 
The algorithm runs in constant space O(1).

An Alternate approach 
Instead of using a two-pointer or a binary search approach, 
we can utilize a HashTable to search for the required pair. 
We can iterate through the array one number at a time. 
Let’s say during our iteration we are at number ‘X’, 
so we need to find ‘Y’ such that “X + Y == TargetX+Y==Target”. 
We will do two things here:

Search for ‘Y’ (which is equivalent to “Target - XTarget−X”) in the HashTable. 
If it is there, we have found the required pair.
Otherwise, insert “X” in the HashTable, so that we can search it for the later numbers.
Here is what our algorithm will look like:
'''

def pair_with_targetsum(arr, target_sum):
  nums = {}  # to store numbers and their indices
  for i, num in enumerate(arr):
    if target_sum - num in nums:
      return [nums[target_sum - num], i]
    else:
      nums[arr[i]] = i
  return [-1, -1]


def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()

'''
Time Complexity 
The time complexity of the above algorithm will be O(N), 
where ‘N’ is the total number of elements in the given array.

Space Complexity 
The space complexity will also be O(N), as, in the worst case, we will be pushing ‘N’ numbers in the HashTable.
'''