'''
Problem Statement 
In a non-empty array of integers, every number appears twice except for one, find that single number.

Example 1:

Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
Example 2:

Input: 7, 9, 7
Output: 9
'''

#mycode
def find_single_number(arr):
  # TODO: Write your code here
  s=0

  for i in arr:
    s=s^i
  return s

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()


#answer
def find_single_number(arr):
  num = 0
  for i in arr:
      num ^= i
  return num

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()


'''
Time Complexity: 
Time complexity of this solution is O(n) as we iterate through all numbers of the input once.

Space Complexity: 
The algorithm runs in constant space O(1).
'''