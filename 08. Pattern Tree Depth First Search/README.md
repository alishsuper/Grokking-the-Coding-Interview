# Pattern 8: Tree Depth First Search (DFS)

This pattern is based on the <b>Depth First Search (DFS)</b> technique to traverse a tree.

We will be using recursion (or we can also use a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing. This also means that the space complexity of the algorithm will be `O(H)`, where `‘H’` is the maximum height of the tree.

## Binary Tree Path Sum (easy)
https://leetcode.com/problems/path-sum/
> Given a binary tree and a number `‘S’`, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals `‘S’`.

As we are trying to search for a root-to-leaf path, we can use the <b>Depth First Search (DFS)</b> technique to solve this problem.

To recursively traverse a binary tree in a DFS fashion, we can start from the root and at every step, make two recursive calls one for the left and one for the right child.

Here are the steps for our Binary Tree Path Sum problem:
1. Start DFS with the root of the tree.
2. If the current node is not a leaf node, do two things:
    - Subtract the value of the current node from the given number to get a new sum => `S = S - node.value`
    - Make two recursive calls for both the children of the current node with the new number calculated in the previous step.
3. At every step, see if the current node being visited is a leaf node and if its value is equal to the given number `‘S’`. If both these conditions are true, we have found the required root-to-leaf path, therefore return `true`.
4. If the current node is a leaf but its value is not equal to the given number `‘S’`, return `false`.

````
class TreeNode {
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
  }
}

function hasPath(root, sum) {
  if(!root) {
    return false
  }
  
  //start DFS with the root of the tree
  //if the current node is a leaf and it's value is
  //equal to the sum then we've found a path
  if(root.value === sum && root.left === null && root.right === null) {
    return true
  }
  
  //recursively call to traverse the left and right sub-tree
  //return true if any of the two recursive calls return true
  return hasPath(root.left, sum - root.value) || hasPath(root.right, sum - root.value)
}

var root = new TreeNode(12)
root.left = new TreeNode(7)
root.right = new TreeNode(1)
root.left.left = new TreeNode(9)
root.right.left = new TreeNode(10)
root.right.right = new TreeNode(5)
console.log(`Tree has path: ${has_path(root, 23)}`)
console.log(`Tree has path: ${has_path(root, 16)}`)
````
- The time complexity of the above algorithm is `O(N)`, where `‘N’` is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
- The space complexity of the above algorithm will be `O(N)` in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child).

## All Paths for a Sum (medium)
https://leetcode.com/problems/path-sum-ii/
> Given a binary tree and a number `‘S’`, find all paths from root-to-leaf such that the sum of all the node values of each path equals `‘S’`.

This problem follows the <b>Binary Tree Path Sum</b> pattern. We can follow the same <b>DFS</b> approach. There will be two differences:
1. Every time we find a root-to-leaf path, we will store it in a list.
2. We will traverse all paths and will not stop processing after finding the first path.

````
class Deque {
    constructor() {
        this.front = this.back = undefined;
    }
    addFront(value) {
        if (!this.front) this.front = this.back = { value };
        else this.front = this.front.next = { value, prev: this.front };
    }
    removeFront() {
        let value = this.peekFront();
        if (this.front === this.back) this.front = this.back = undefined;
        else (this.front = this.front.prev).next = undefined;
        return value;
    }
    peekFront() { 
        return this.front && this.front.value;
    }
    addBack(value) {
        if (!this.front) this.front = this.back = { value };
        else this.back = this.back.prev = { value, next: this.back };
    }
    removeBack() {
        let value = this.peekBack();
        if (this.front === this.back) this.front = this.back = undefined;
        else (this.back = this.back.next).back = undefined;
        return value;
    }
    peekBack() { 
        return this.back && this.back.value;
    }
}

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null; 
  }
};


function find_paths(root, sum) {
  //Every time we find a root-to-leaf path, we will store it in a list.
  allPaths = [];
//We will traverse all paths and will not stop processing after finding the first path.
 findPathsRecursive(root, sum, new Deque(), allPaths)
  return allPaths;
};

function findPathsRecursive(currentNode, sum, currentPath, allPaths){
  if(currentNode === null) return
  
  //add the current node to the path
  currentPath.push(currentNode.value)
  
  //if the current node is a leaf and it's value is equal to sum, save the current path
  if(currentNode.val === sum && currentNode.left === null & currentNode.right === null) {
    allPaths.push(currentPath.toArray())
  } else {
    //traverse the left sub-tree
    findPathsRecursive(currentNode.left, sum - currentNode.value, currentPath, allPaths)
    //traverse the right sub-tree
    findPathsRecursive(currentNode.right, sum - currentNode.value, currentPath, allPaths)
  }
  //remove the current node from the path to backtrack,
  //we need to remove the current node while we are going up the recursive call stack
  currentPath.pop()
}



var root = new TreeNode(12)
root.left = new TreeNode(7)
root.right = new TreeNode(1)
root.left.left = new TreeNode(4)
root.right.left = new TreeNode(10)
root.right.right = new TreeNode(5)
let sum = 23,
  result = find_paths(root, sum);

process.stdout.write(`Tree paths with sum ${sum}: `);
for (i = 0; i < result.length; i++) {
  process.stdout.write(`[${result[i]}] `);
}
````
- The time complexity of the above algorithm is `O(N^2)`, where `‘N’` is the total number of nodes in the tree. This is due to the fact that we traverse each node once (which will take `O(N)`), and for every leaf node, we might have to store its path (by making a copy of the current path) which will take `O(N)`.
  - We can calculate a tighter time complexity of `O(NlogN)` from the space complexity discussion below.
- If we ignore the space required for the `allPaths` list, the space complexity of the above algorithm will be `O(N)` in the worst case. This space will be used to store the recursion stack. The worst-case will happen when the given tree is a linked list (i.e., every node has only one child).

> 🌟 Given a binary tree, return all root-to-leaf paths.

Solution: We can follow a similar approach. We just need to remove the “check for the path sum.”

> 🌟 Given a binary tree, find the root-to-leaf path with the maximum sum.

Solution: We need to find the path with the maximum sum. As we traverse all paths, we can keep track of the path with the maximum sum.

## Sum of Path Numbers (medium)
https://leetcode.com/problems/sum-root-to-leaf-numbers/
> Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.

This problem follows the <b>Binary Tree Path Sum</b> pattern. We can follow the same <b>DFS</b> approach. The additional thing we need to do is to keep track of the number representing the current path.

How do we calculate the path number for a node? Taking the first example mentioned above, say we are at node ‘7’. As we know, the path number for this node is ‘17’, which was calculated by: `1 * 10 + 7 => 17`. We will follow the same approach to calculate the path number of each node.

````
class TreeNode {
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
  }
}

function findSumOfPathNumbers(root) {
  return findRootToLeafPathNumbers(root, 0)
}

function findRootToLeafPathNumbers(currentNode, pathSum) {
    if(currentNode === null) {
      return 0
    } 
    
    //calculate the path number of the current node
    pathSum = 10 * pathSum + currentNode.value
    
    //if the currentNode is a leaf, retuen the current pathSum
    if(currentNode.left === null && currentNode.right === null) {
      return pathSum
    }
    
    //traverse the left and the right sub-tree
    return findRootToLeafPathNumbers(currentNode.left, pathSum) + findRootToLeafPathNumbers(currentNode.right, pathSum)
}

const root = new TreeNode(1)
root.left = new TreeNode(0)
root.right = new TreeNode(1)
root.left.left = new TreeNode(1)
root.right.left = new TreeNode(6)
root.right.right = new TreeNode(5)
console.log(`Total Sum of Path Numbers: ${findSumOfPathNumbers(root)}`)
````
- The time complexity of the above algorithm is `O(N)`, where `‘N’` is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
- The space complexity of the above algorithm will be `O(N)` in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
## Path With Given Sequence (medium)
> Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

This problem follows the <b>Binary Tree Path Sum</b> pattern. We can follow the same <b>DFS</b> approach and additionally, track the element of the given sequence that we should match with the current node. Also, we can return false as soon as we find a mismatch between the sequence and the node value.
````
class TreeNode {
  constructor(value) {
    this.value = value
    this.right = null
    this.left = null
  }
}

function findPath(root, sequence) {
  if(!root) {
    return sequence.length === 0
  }
  
  return findPathRecursive(root, sequence, 0)
}

function findPathRecursive(currentNode, sequence, sequenceIndex) {
  if(currentNode === null) return false
  
  const sequenceLength = sequence.length
  if(sequenceIndex >= sequenceLength || currentNode.value !== sequence[sequenceIndex]) return false
  
  //if the current node is a leaf, and it is the end of the sequence, then we have found a path
  if(currentNode.left === null && currentNode.right === null && sequenceIndex === sequenceLength - 1) return true
  
  //recursively call to traverse the left and right sub-tree
  //return true if any of the two recursive calls return true
  
  return findPathRecursive(currentNode.left, sequence, sequenceIndex + 1) || findPathRecursive(currentNode.right, sequence, sequenceIndex + 1)
}

const root = new TreeNode(1)
root.left = new TreeNode(0)
root.right = new TreeNode(1)
root.left.left = new TreeNode(1)
root.right.left = new TreeNode(6)
root.right.right = new TreeNode(5)

console.log(`Tree has path sequence: ${findPath(root, [1, 0, 7])}`)
console.log(`Tree has path sequence: ${findPath(root, [1, 1, 6])}`)
````
- The time complexity of the above algorithm is `O(N)`, where `‘N’` is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
- The space complexity of the above algorithm will be `O(N)` in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
## Count Paths for a Sum (medium)
https://leetcode.com/problems/path-sum-iii/

> Given a binary tree and a number `‘S’`, find all paths in the tree such that the sum of all the node values of each path equals `‘S’`. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

This problem follows the <b>Binary Tree Path Sum</b> pattern. We can follow the same <b>DFS</b> approach. But there will be four differences:
1. We will keep track of the current path in a list which will be passed to every recursive call.
2. Whenever we traverse a node we will do two things:

    - Add the current node to the current path.
    - As we added a new node to the current path, we should find the sums of all sub-paths ending at the current node. If the sum of any sub-path is equal to ‘S’ we will increment our path count.
3. We will traverse all paths and will not stop processing after finding the first path.
4. Remove the current node from the current path before returning from the function. This is needed to Backtrack while we are going up the recursive call stack to process other paths.
````
class TreeNode {
  constructor(value, right = null, left = null) {
    this.value = value
    this.right = right
    this.left = left
  }
}

function countPaths(root, S) {
  let currentPath = []
  return countPathsRecursive(root, S, currentPath)
}

function countPathsRecursive(currentNode, S, currentPath) {
  if(currentNode === null) return 0
  
  //add the currentNode to the path
  currentPath.push(currentNode.value)
  
  let pathCount = 0
  let pathSum = 0
  
  //find the sums of all aub-paths in the current path list
  for(let i = currentPath.length - 1; i >= 0; i--) {
    pathSum += currentPath[i]
    
    //if the sum of any sub-path is equal S we increment our path count
    if(pathSum === S) {
      pathCount++
    }
  }
  
  //traverse the left sub-tree
  pathCount += countPathsRecursive(currentNode.left, S, currentPath)
  //traverse the right sub-tree
  pathCount += countPathsRecursive(currentNode.right, S, currentPath)
  
  //remove the current node from the path to backtrack
  //we need to remove the current node while we are going upp the recursive call stack
  currentPath.pop()
  return pathCount
}

const root = new TreeNode(12)
root.left = new TreeNode(7)
root.right = new TreeNode(1)
root.left.left = new TreeNode(4)
root.right.left = new TreeNode(10)
root.right.right = new TreeNode(5)
console.log(`Tree has ${countPaths(root, 11)} paths`)
````
- The time complexity of the above algorithm is `O(N²)` in the worst case, where `‘N’` is the total number of nodes in the tree. This is due to the fact that we traverse each node once, but for every node, we iterate the current path. The current path, in the worst case, can be `O(N)` (in the case of a skewed tree). But, if the tree is balanced, then the current path will be equal to the height of the tree, i.e., `O(logN)`. So the best case of our algorithm will be `O(NlogN)`.
- The space complexity of the above algorithm will be `O(N)`. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child). We also need `O(N)` space for storing the currentPath in the worst case.  Overall space complexity of our algorithm is `O(N)`.
## 🌟 Tree Diameter (medium)
https://leetcode.com/problems/diameter-of-binary-tree/
## 🌟 Path with Maximum Sum (hard)
https://leetcode.com/problems/binary-tree-maximum-path-sum/
