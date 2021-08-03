'''
Problem Challenge 2
Search in Rotated Array (medium)

Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, 
find if a given ‘key’ is present in it.

Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. 
You can assume that the given array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.

Example 2:

Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.
'''

#mycode
def search_rotated_array(arr, key):
  # TODO: Write your code here
  start, end = 0, len(arr)-1
  while start <= end:
    mid= (start + end) //2
    if arr[mid] == key:
      return mid
    
    if arr[start] <= arr[mid]:
      if arr[start] <= key and arr[mid] > key:
        end = mid-1
      else:
        start = mid+1
    else:
      if key > arr[end] or key < arr[mid]:
        end = mid - 1
      else:
        start = mid + 1
  return -1


def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()




#answer
def search_rotated_array(arr, key):
  start, end = 0, len(arr) - 1
  while start <= end:
    mid = start + (end - start) // 2
    if arr[mid] == key:
      return mid

    if arr[start] <= arr[mid]:  # left side is sorted in ascending order
      if key >= arr[start] and key < arr[mid]:
        end = mid - 1
      else:  # key > arr[mid]
        start = mid + 1
    else:  # right side is sorted in ascending order
      if key > arr[mid] and key <= arr[end]:
        start = mid + 1
      else:
        end = mid - 1

  # we are not able to find the element in the given array
  return -1


def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

main()


'''
Time complexity 
Since we are reducing the search range by half at every step, 
this means that the time complexity of our algorithm will be O(logN) 
where ‘N’ is the total elements in the given array.

Space complexity 
The algorithm runs in constant space O(1).
'''


'''
Similar Problems 
Problem 1 
How do we search in a sorted and rotated array that also has duplicates?

The code above will fail in the following example!

Example 1:

Input: [3, 7, 3, 3, 3], key = 7
Output: 1
Explanation: '7' is present in the array at index '1'.

Solution 
The only problematic scenario is when the numbers at indices start, middle, and end are the same, as in this case,
we can’t decide which part of the array is sorted. 
In such a case, the best we can do is to skip one number from both ends: start = start + 1 & end = end - 1.
'''


def search_rotated_with_duplicates(arr, key):
  start, end = 0, len(arr) - 1
  while start <= end:
    mid = start + (end - start) // 2
    if arr[mid] == key:
      return mid

    # the only difference from the previous solution,
    # if numbers at indexes start, mid, and end are same, we can't choose a side
    # the best we can do, is to skip one number from both ends as key != arr[mid]
    if arr[start] == arr[mid] and arr[end] == arr[mid]:
      start += 1
      end -= 1
    elif arr[start] <= arr[mid]:  # left side is sorted in ascending order
      if key >= arr[start] and key < arr[mid]:
        end = mid - 1
      else:  # key > arr[mid]
        start = mid + 1

    else:  # right side is sorted in ascending order
      if key > arr[mid] and key <= arr[end]:
        start = mid + 1
      else:
        end = mid - 1

  # we are not able to find the element in the given array
  return -1


def main():
  print(search_rotated_with_duplicates([3, 7, 3, 3, 3], 7))


main()
