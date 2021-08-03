'''
Problem Challenge 1

Quadruple Sum to Target (medium) 
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

Example 1:

Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.

Example 2:

Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.
'''

#mycode
def search_quadruplets(arr, target):
  quadruplets = []
  # TODO: Write your code here

  arr.sort()

  for i in range(len(arr)-3):
    if i>0 and arr[i] == arr[i-1]:
      continue
    for j in range(i+1,len(arr)-2):
      if j>i and arr[j] == arr[j-1]:
        continue
      search_pair(arr, i, j, target, quadruplets)

  return quadruplets

def search_pair(arr, i, j, target, quadruplets):
  left = j+1
  right = len(arr) - 1

  sub_target=target - arr[i] - arr[j]

  while left < right:
    if arr[left] + arr[right] == sub_target:
      quadruplets.append([arr[i],arr[j],arr[left],arr[right]])
      left += 1
      right -= 1

      while left < right and arr[left] == arr[left-1]:
        left += 1
      
      while left < right and arr[right] == arr[right+1]:
        right -=1
    elif arr[left] + arr[right] < sub_target:
      left += 1
    else:
      right -= 1



#answer
def search_quadruplets(arr, target):
  arr.sort()
  quadruplets = []
  for i in range(0, len(arr)-3):
    # skip same element to avoid duplicate quadruplets
    if i > 0 and arr[i] == arr[i - 1]:
      continue
    for j in range(i + 1, len(arr)-2):
      # skip same element to avoid duplicate quadruplets
      if j > i + 1 and arr[j] == arr[j - 1]:
        continue
      search_pairs(arr, target, i, j, quadruplets)
  return quadruplets


def search_pairs(arr, target_sum, first, second, quadruplets):
  left = second + 1
  right = len(arr) - 1
  while (left < right):
    sum = arr[first] + arr[second] + arr[left] + arr[right]
    if sum == target_sum:  # found the quadruplet
      quadruplets.append(
        [arr[first], arr[second], arr[left], arr[right]])
      left += 1
      right -= 1
      while (left < right and arr[left] == arr[left - 1]):
        left += 1  # skip same element to avoid duplicate quadruplets
      while (left < right and arr[right] == arr[right + 1]):
        right -= 1  # skip same element to avoid duplicate quadruplets
    elif sum < target_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum


def main():
  print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
  print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()



'''
Time complexity 
Sorting the array will take O(N*logN). Overall searchQuadruplets() will take O(N * logN + N^3), which is asymptotically equivalent to O(N^3).

Space complexity 
The space complexity of the above algorithm will be O(N) which is required for sorting.

'''