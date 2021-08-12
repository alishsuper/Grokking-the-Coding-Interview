'''
Triplet Sum Close to Target (medium)

Problem Statement 
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. 
If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
'''

#mycode
import math

def triplet_sum_close_to_target(arr, target_sum):
  
  # TODO: Write your code here
  arr.sort()
  min_sum, err_min = 0, math.inf

  for i in range(len(arr)):
    j, k = i+1, len(arr)-1
    while j < k:
      err = abs(arr[i]+arr[j]+arr[k]-target_sum)
      if err < err_min:
        err_min=err
        min_sum = arr[i]+arr[j]+arr[k]
      elif err == err_min:
        min_sum=min(min_sum,arr[i]+arr[j]+arr[k])

      if arr[i]+arr[j]+arr[k] < target_sum:
        j += 1
      elif arr[i]+arr[j]+arr[k] > target_sum:
        k -= 1

  return min_sum



#answer
import math
def triplet_sum_close_to_target(arr, target_sum):
  arr.sort()
  smallest_difference = math.inf
  for i in range(len(arr)-2):
    left = i + 1
    right = len(arr) - 1
    while (left < right):
      target_diff = target_sum - arr[i] - arr[left] - arr[right]
      if target_diff == 0:  # we've found a triplet with an exact sum
        return target_sum - target_diff  # return sum of all the numbers

      # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
      if abs(target_diff) < abs(smallest_difference) or (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
        smallest_difference = target_diff  # save the closest and the biggest difference

      if target_diff > 0:
        left += 1  # we need a triplet with a bigger sum
      else:
        right -= 1  # we need a triplet with a smaller sum

  return target_sum - smallest_difference


def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()


'''
Time complexity 
Sorting the array will take O(N* logN)O(N∗logN). Overall searchTriplet() will take O(N * logN + N^2), 
which is asymptotically equivalent to O(N^2).

Space complexity 
The space complexity of the above algorithm will be O(N) which is required for sorting.
'''