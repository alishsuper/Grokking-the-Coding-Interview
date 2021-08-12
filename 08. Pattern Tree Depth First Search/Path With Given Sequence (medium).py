'''
Problem Statement 
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
'''

#mycode
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  # TODO: Write your code here
  
  return find_current_path(root, sequence)

def find_current_path(currentNode, sequence):
  
  if not currentNode:
    return False

  if currentNode.val != sequence[0]:
    return False
  else:
    if currentNode.left is None and currentNode.right is None:
      return True
    else:
      del sequence[0]
      return find_current_path(currentNode.left, sequence) or find_current_path(currentNode.right, sequence)
  



def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()



#answer
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  if not root:
    return len(sequence) == 0

  return find_path_recursive(root, sequence, 0)


def find_path_recursive(currentNode, sequence, sequenceIndex):

  if currentNode is None:
    return False

  seqLen = len(sequence)
  if sequenceIndex >= seqLen or currentNode.val != sequence[sequenceIndex]:
    return False

  # if the current node is a leaf, add it is the end of the sequence, we have found a path!
  if currentNode.left is None and currentNode.right is None and sequenceIndex == seqLen - 1:
    return True

  # recursively call to traverse the left and right sub-tree
  # return true if any of the two recursive call return true
  return find_path_recursive(currentNode.left, sequence, sequenceIndex + 1) or \
         find_path_recursive(currentNode.right, sequence, sequenceIndex + 1)


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()


'''
Time complexity 
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. 
This is due to the fact that we traverse each node once.

Space complexity 
The space complexity of the above algorithm will be O(N) in the worst case. 
This space will be used to store the recursion stack. 
The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
'''