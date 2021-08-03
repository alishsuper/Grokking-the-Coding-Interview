'''
Problem Challenge 1
Search Bitonic Array (medium) 
Given a Bitonic array, find if a given ‘key’ is present in it. 
An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 
Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

Example 1:

Input: [1, 3, 8, 4, 3], key=4
Output: 3

Example 2:

Input: [3, 8, 3, 1], key=8
Output: 1

Example 3:

Input: [1, 3, 8, 12], key=12
Output: 3

Example 4:

Input: [10, 9, 8], key=10
Output: 0
'''


#mycode
def search_bitonic_array(arr, key):
  # TODO: Write your code here
  maxIndex = search_maximum(arr)
  if key > arr[maxIndex]:
    return -1
  start, end = 0, maxIndex

  while start <= end:
    mid = (start + end) //2
    if arr[mid] < key:
      start = mid + 1
    elif arr[mid] > key:
      end = mid - 1
    else:
      return mid
  
  start, end = maxIndex, len(arr)-1
  while start <= end:
    mid = (start + end) //2
    if arr[mid] < key:
      end = mid - 1
    elif arr[mid] > key:
      start = mid + 1
    else:
      return mid

  return -1

def search_maximum(arr):
  start, end = 0, len(arr)-1
  while start < end:
    mid = (start + end) //2
    if arr[mid] < arr[mid+1]:
      start = mid+1
    else:
      end = mid
    
  return start

def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()



#answer
def search_bitonic_array(arr, key):
  maxIndex = find_max(arr)
  keyIndex = binary_search(arr, key, 0, maxIndex)
  if keyIndex != -1:
    return keyIndex
  return binary_search(arr, key, maxIndex + 1, len(arr) - 1)


# find index of the maximum value in a bitonic array
def find_max(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2
    if arr[mid] > arr[mid + 1]:
      end = mid
    else:
      start = mid + 1

  # at the end of the while loop, 'start == end'
  return start


# order-agnostic binary search
def binary_search(arr, key, start, end):
  while start <= end:
    mid = int(start + (end - start) / 2)

    if key == arr[mid]:
      return mid

    if arr[start] < arr[end]:  # ascending order
      if key < arr[mid]:
        end = mid - 1
      else:  # key > arr[mid]
        start = mid + 1
    else:  # descending order
      if key > arr[mid]:
        end = mid - 1
      else:  # key < arr[mid]
        start = mid + 1

  return -1  # element is not found


def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()


'''
Time complexity 
Since we are reducing the search range by half at every step, 
this means that the time complexity of our algorithm will be O(logN) 
where ‘N’ is the total elements in the given array.

Space complexity 
The algorithm runs in constant space O(1).
'''