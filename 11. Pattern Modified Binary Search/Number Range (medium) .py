'''
Problem Statement 
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

Example 1:

Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]

Example 2:

Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]

Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]
'''

#mycode
def find_range(arr, key):
  result = [- 1, -1]
  # TODO: Write your code here
  result[0]=binary_search(arr, key, False)
  if result[0] != -1:
    result[1]=binary_search(arr, key, True)
  return result


def binary_search(arr, key, findMax):
  start, end = 0, len(arr)-1

  keyIndex = -1
  while start <= end:
    mid = (start + end) //2

    if arr[mid] < key:
      start = mid+1
    elif arr[mid] > key:
      end = mid - 1
    else:
      keyIndex = mid
      if findMax:
        start = mid +1
      else:
        end = mid - 1

  return keyIndex

def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()



#answer
def find_range(arr, key):
  result = [- 1, -1]
  result[0] = binary_search(arr, key, False)
  if result[0] != -1:  # no need to search, if 'key' is not present in the input array
    result[1] = binary_search(arr, key, True)
  return result


# modified Binary Search
def binary_search(arr, key, findMaxIndex):
  keyIndex = -1
  start, end = 0, len(arr) - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < arr[mid]:
      end = mid - 1
    elif key > arr[mid]:
      start = mid + 1
    else:  # key == arr[mid]
      keyIndex = mid
      if findMaxIndex:
        start = mid + 1  # search ahead to find the last index of 'key'
      else:
        end = mid - 1  # search behind to find the first index of 'key'

  return keyIndex


def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()



'''
Time complexity 
Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm 
will be O(logN) where ‘N’ is the total elements in the given array.

Space complexity 
The algorithm runs in constant space O(1).
'''