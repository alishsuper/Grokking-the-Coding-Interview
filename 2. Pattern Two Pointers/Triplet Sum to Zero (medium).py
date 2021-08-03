'''
Problem Statement 
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
'''


#mycode 
def search_triplets(arr):
  triplets = []
  arr.sort()
  # TODO: Write your code here
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:
      continue
    search_pair(arr, -arr[i], i+1, triplets)

  return triplets

def search_pair(arr, target_sum, left, triplets):
  right = len(arr)-1
  while left < right:
    if arr[left] + arr[right] == target_sum:
      triplets.append([-target_sum, arr[left], arr[right]])
      left += 1
      right -= 1

      while left < right and arr[left] == arr[left-1]:
        left += 1
      while left < right and arr[right] == arr[right+1]:
        right -= 1

    elif arr[left] + arr[right] > target_sum:
      right -=1
    else:
      left += 1



#answer
def search_triplets(arr):
  arr.sort()
  triplets = []
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
      continue
    search_pair(arr, -arr[i], i+1, triplets)

  return triplets


def search_pair(arr, target_sum, left, triplets):
  right = len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:  # found the triplet
      triplets.append([-target_sum, arr[left], arr[right]])
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left - 1]:
        left += 1  # skip same element to avoid duplicate triplets
      while left < right and arr[right] == arr[right + 1]:
        right -= 1  # skip same element to avoid duplicate triplets
    elif target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum


def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()


'''
Time complexity 
Sorting the array will take O(N * logN). 
The searchPair() function will take O(N). 
As we are calling searchPair() for every number in the input array, 
this means that overall searchTriplets() will take O(N * logN + N^2), which is asymptotically equivalent to O(N^2).

Space complexity 
Ignoring the space required for the output array, 
the space complexity of the above algorithm will be O(N) which is required for sorting.
'''