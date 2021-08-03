'''
Problem Statement 
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n!n! permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
'''

#mycode
from collections import deque

def find_permutations(nums):
  result = []
  # TODO: Write your code here
  currentPermutation = deque()
  currentPermutation.append([])

  for num in nums:
    for i in range(len(currentPermutation)):
      previousPermutation = currentPermutation.popleft()
      for j in range(len(previousPermutation)+1):
        newPermutation = previousPermutation.copy()
        newPermutation.insert(j, num)

        if len(newPermutation) == len(nums):
          result.append(newPermutation)
        else:
          currentPermutation.append(newPermutation)
          


  return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()




#answer
from collections import deque


def find_permutations(nums):
  numsLength = len(nums)
  result = []
  permutations = deque()
  permutations.append([])
  for currentNumber in nums:
    # we will take all existing permutations and add the current number to create new permutations
    n = len(permutations)
    for _ in range(n):
      oldPermutation = permutations.popleft()
      # create a new permutation by adding the current number at every position
      for j in range(len(oldPermutation)+1):
        newPermutation = list(oldPermutation)
        newPermutation.insert(j, currentNumber)
        if len(newPermutation) == numsLength:
          result.append(newPermutation)
        else:
          permutations.append(newPermutation)

  return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()


'''
Time complexity 
We know that there are a total of N! permutations of a set with ‘N’ numbers. 
In the algorithm above, we are iterating through all of these permutations with the help of the two ‘for’ loops. 
In each iteration, we go through all the current permutations to insert a new number in them on line 17 (line 23 for C++ solution). 
To insert a number into a permutation of size ‘N’ will take O(N),
which makes the overall time complexity of our algorithm O(N*N!).

Space complexity 
All the additional space used by our algorithm is for the result list and the queue to store the intermediate permutations. 
If you see closely, at any time, we don’t have more than N! permutations between the result list and the queue. 
Therefore the overall space complexity to store N! permutations each containing NN elements will be O(N*N!).
'''


#recursive solution
def generate_permutations(nums):
  result = []
  generate_permutations_recursive(nums, 0, [], result)
  return result


def generate_permutations_recursive(nums, index, currentPermutation, result):
  if index == len(nums):
    result.append(currentPermutation)
  else:
    # create a new permutation by adding the current number at every position
    for i in range(len(currentPermutation)+1):
      newPermutation = list(currentPermutation)
      newPermutation.insert(i, nums[index])
      generate_permutations_recursive(
        nums, index + 1, newPermutation, result)


def main():
  print("Here are all the permutations: " + str(generate_permutations([1, 3, 5])))


main()
