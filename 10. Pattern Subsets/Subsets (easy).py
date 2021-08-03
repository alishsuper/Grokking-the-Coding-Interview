'''
Problem Statement 
Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
'''


#mycode
def find_subsets(nums):
  subsets = []
  subsets.append([])

  for currentNumber in nums:
    for i in range(len(subsets)):
      j = subsets[i].copy()
      j.append(currentNumber)
      subsets.append(j)

  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()


#answer
def find_subsets(nums):
  subsets = []
  # start by adding the empty subset
  subsets.append([])
  for currentNumber in nums:
    # we will take all existing subsets and insert the current number in them to create new subsets
    n = len(subsets)
    for i in range(n):
      # create a new subset from the existing subset and insert the current element to it
      set = subsets[i].copy()
      set.append(currentNumber)
      subsets.append(set)

  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()


'''
Time complexity 
Since, in each step, the number of subsets doubles as we add each element to all the existing subsets, the time complexity of the above algorithm is O(2^N), 
where ‘N’ is the total number of elements in the input set. This also means that, in the end, we will have a total of O(2^N) subsets.

Space complexity 
All the additional space used by our algorithm is for the output list. Since we will have a total of O(2^N) subsets, 
the space complexity of our algorithm is also O(2^N).
'''