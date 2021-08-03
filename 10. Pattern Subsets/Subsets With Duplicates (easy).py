'''
Problem Statement 
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]

Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
'''

#mycode
def find_subsets(nums):
  subsets = []
  # TODO: Write your code here
  subsets.append([])

  start, end = 0, 0
  for i in range(len(nums)):
    start = 0
    if i>0 and nums[i] == nums[i-1]:
      start = end 
    end = len(subsets) 

    for j in range(start, end):
      set = subsets[j].copy()
      set.append(nums[i])
      subsets.append(set)

  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()



#answer
def find_subsets(nums):
  # sort the numbers to handle duplicates
  list.sort(nums)
  subsets = []
  subsets.append([])
  startIndex, endIndex = 0, 0
  for i in range(len(nums)):
    startIndex = 0
    # if current and the previous elements are same, create new subsets only from the subsets
    # added in the previous step
    if i > 0 and nums[i] == nums[i - 1]:
      startIndex = endIndex + 1
    endIndex = len(subsets) - 1
    for j in range(startIndex, endIndex+1):
      # create a new subset from the existing subset and add the current element to it
      set = list(subsets[j])
      set.append(nums[i])
      subsets.append(set)
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()


'''
Time complexity 
Since, in each step, the number of subsets could double (if not duplicate) as we add each element to all the existing subsets, 
the time complexity of the above algorithm is O(2^N), where ‘N’ is the total number of elements in the input set. 
This also means that, in the end, we will have a total of O(2^N) subsets at the most.

Space complexity 
All the additional space used by our algorithm is for the output list. Since at most we will have a total of O(2^N) subsets, 
the space complexity of our algorithm is also O(2^N).
'''