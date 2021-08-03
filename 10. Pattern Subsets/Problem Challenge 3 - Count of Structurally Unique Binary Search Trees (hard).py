'''
Problem Challenge 3

Count of Structurally Unique Binary Search Trees (hard)

Given a number ‘n’, write a function to return the count of structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’.

Example 1:

Input: 2
Output: 2
Explanation: As we saw in the previous problem, there are 2 unique BSTs storing numbers from 1-2.

Example 2:

Input: 3
Output: 5
Explanation: There will be 5 unique BSTs that can store numbers from 1 to 5.
'''


#mycode
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def count_trees(n):
  if n < 0:
    return -1
  if n <=1 :
    return 1

  count = 0  
  for i  in range(1,n+1):
    left = count_trees(i-1)
    right = count_trees(n-i)
    count += left * right
  return count


def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))


main()


#answer
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def count_trees(n):
  return count_trees_rec({}, n)


def count_trees_rec(map, n):
  if n in map:
    return map[n]

  if n <= 1:
    return 1
  count = 0
  for i in range(1, n+1):
    # making 'i' the root of the tree
    countOfLeftSubtrees = count_trees_rec(map, i - 1)
    countOfRightSubtrees = count_trees_rec(map, n - i)
    count += (countOfLeftSubtrees * countOfRightSubtrees)

  map[n] = count
  return count


def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))


main()



'''
Time complexity #
The time complexity of this algorithm will be exponential and will be similar to Balanced Parentheses. 
Estimated time complexity will be O(n*2^n) but the actual time complexity ( O(4^n/\sqrt{n})) 
is bounded by the Catalan number and is beyond the scope of a coding interview. 

Space complexity 
The space complexity of this algorithm will be exponential too, estimated O(2^n) but the actual will be (O(4^n/\sqrt{n}).

Memorized version 
Our algorithm has overlapping subproblems as our recursive call will be evaluating the same sub-expression multiple times. 
To resolve this, we can use memorization and store the intermediate results in a HashMap. 
In each function call, we can check our map to see if we have already evaluated this sub-expression before. 
'''
