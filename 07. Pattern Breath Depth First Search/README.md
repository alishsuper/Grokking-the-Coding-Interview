# Pattern 7: Tree Breadth First Search

This pattern is based on the <b>Breadth First Search (BFS)</b> technique to traverse a tree.

Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. We will use a <b>Queue</b> to keep track of all the nodes of a level before we jump onto the next level. This also means that the space complexity of the algorithm will be `O(W)`, where `W` is the maximum number of nodes on any level.


## Binary Tree Level Order Traversal (easy) 😕
https://leetcode.com/problems/binary-tree-level-order-traversal/

> Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all <b>nodes of each level from left to right</b> in separate sub-arrays.

Since we need to traverse all nodes of each level before moving onto the next level, we can use the <b>Breadth First Search (BFS)</b> technique to solve this problem.

We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:
1. Start by pushing the `root` node to the queue.
2. Keep iterating until the queue is empty.
3. In each iteration, first count the elements in the queue (let’s call it `levelSize`). We will have these many nodes in the current level.
4. Next, remove `levelSize` nodes from the queue and push their `value` in an array to represent the current level.
5. After removing each node from the queue, insert both of its children into the queue.
6. If the queue is not empty, repeat from step 3 for the next level.

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


function traverse (root) {
  result = [];
  if(root === null ) {
    return result
  }
  
  const queue = new Deque()
  //Start by pushing the root node to the queue.
  queue.addFront(root)
  //Keep iterating until the queue is empty.
  let currentLevel = []
  while (queue.length > 0) {
    const levelSize = queue.length
    //In each iteration, first count the elements in the queue (let’s call it levelSize). We will have these many nodes in the current level.
     
    for(i = 0; i < levelSize; i++) {
      TreeNode = queue.removeFront()
      //add the node to the current level
      currentLevel.push(TreeNode.val)
      //insert the children of current node in the queue
      if(TreeNode.left !== null) {
        queue.addBack(TreeNode.left)
      }
    }
    if(TreeNode.right !== null) {
      queue.addBack(TreeNode.right)
    }
  }
  
  result.push(currentLevel)
  
  //Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
  //After removing each node from the queue, insert both of its children into the queue.
  //If the queue is not empty, repeat from step 3 for the next level.
  return result;
};



var root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
console.log(`Level order traversal: ${traverse(root)}`);
````

- The time complexity of the above algorithm is `O(N)`, where `N` is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
- The space complexity of the above algorithm will be `O(N)` as we need to return a list containing the level order traversal. We will also need `O(N)` space for the queue. Since we can have a maximum of `N/2` nodes at any level (this could happen only at the lowest level), therefore we will need `O(N)` space to store them in the queue.

### Easier to understand solution w/o `Deque()`
````
function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
 }
 
 const levelOrder = function  (root) {
  //If root is null return an empty array
  if(!root) return []
  
  const queue = [root] //initialize the queue with root
  const levels = [] //declare output array
  
  while(queue.length !== 0) {
    const queueLength = queue.length//get the length prior to deque
    const currLevel = []//declare this level
    //loop through to exahuast all options and only to include nodes at currLevel
    for(let i = 0; i < queueLength; i++) {
      //get next node
      const current = queue.shift()
      if(current.left) {
        queue.push(current.left)
      }
      if(current.right) {
        queue.push(current.right)
      }
      //after we add left and right for current, we add to currLevel
      currLevel.push(current.val)
    }
    //Level has been finished. Push into output array
    levels.push(currLevel) 
  }
  return levels
};

levelOrder([3,9,20,null,null,15,7])//[[3],[9,20],[15,7]]
levelOrder([1])//[[1]]
levelOrder([])//[]
````

## Reverse Level Order Traversal (easy)
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
> Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., <b>the lowest level comes first</b>. You should populate the values of all nodes in each level from left to right in separate sub-arrays.

This problem follows the <b>Binary Tree Level Order Traversal</b> pattern. We can follow the same <b>BFS</b> approach. The only difference will be that instead of appending the current level at the end, we will append the current level at the beginning of the result list.
````
function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
 }
 
 const traverse = function(root) {
  if(!root) return []
   const queue = [root]
   
   const levels = []
   
   while(queue.length !== 0) {
     const queueLength = queue.length
     const currLevel = []
     for (let i = 0; i < queueLength; i++) {
       const current = queue.push()
       if(current.left) {
         queue.push(current.left)
       }
       if(current.right) {
         queue.push(current.right)
       }
       currLevel.push(current.val)
     }
     levels.unshift(currLevel)
   }
   
   return levels
}
 
 traverse([[12], [7,1], [9, 10, null, 5]])
````
- The time complexity of the above algorithm is `O(N)`, where `N` is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
- The space complexity of the above algorithm will be `O(N)` as we need to return a list containing the level order traversal. We will also need `O(N)` space for the queue. Since we can have a maximum of `N/2` nodes at any level (this could happen only at the lowest level), therefore we will need `O(N)` space to store them in the queue.

## Zigzag Traversal (medium) 🌴
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

> Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all <b>nodes of the first level from left to right</b>, then <b>right to left for the next level</b> and keep alternating in the same manner for the following levels.

This problem follows the <b>Binary Tree Level Order Traversal</b> pattern. We can follow the same <b>BFS</b> approach. The only additional step we have to keep in mind is to alternate the level order traversal, which means that for every other level, we will traverse similar to <b>Reverse Level Order Traversal</b>.


````
function TreeNode(val, left, right) {
  this.val = (val === undefined ? 0 : val)
  this.left = (left === undefined ? null : left)
  this.right = (right === undefined ? nill : right)
}

function zigzagLevelOrder(root) {
  //if root is null return an empty array
  if(!root) return []
  
  //initialize the queue with root
  const queue = [root]
  //declare the output array
  const levels = []
  let leftToRight = true
  
  while(queue.length !== 0) {
    //get the length prior to deque?
    const queueLength = queue.length
    //declare the current level
    const currentLevel = []
    
    //loop through to exhaust all aoption and only to include nodes at current Level
    for (let i = 0; i < queueLength; i++) {
      //get the next node
      const currentNode = queue.shift()
      
      //add the node to the current level based on the traverse direction
      if(leftToRight) {
        currentLevel.push(currentNode.val)
      } else {
        currentLevel.unshift(currentNode.val)
      }
      
      //insert the children of current node in the queue
      if(currentNode.left !== null) {
        queue.push(currentNode.left) 
      }
      if(currentNode.right !== null) {
        queue.push(currentNode.right)
      }
    }
    //Level has been finished. push to the out put arra
    levels.push(currentLevel)
    
    //reverse the traversal direction 
    leftToRight = !leftToRight
  }
  return levels
}

zigzagLevelOrder([1, 2, 3, 4, 5, 6, 7])
zigzagLevelOrder([3,9,20,null,null,15,7])
zigzagLevelOrder([1])
zigzagLevelOrder([])
````
- The time complexity of the above algorithm is `O(N)`, where `N` is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
- The space complexity of the above algorithm will be `O(N)` as we need to return a list containing the level order traversal. We will also need `O(N)` space for the queue. Since we can have a maximum of `N/2` nodes at any level (this could happen only at the lowest level), therefore we will need `O(N)` space to store them in the queue.

## Level Averages in a Binary Tree (easy)
https://leetcode.com/problems/average-of-levels-in-binary-tree/

> Given a binary tree, populate an array to represent the <b>averages of all of its levels</b>

This problem follows the <b>Binary Tree Level Order Traversal</b> pattern. We can follow the same <b>BFS</b> approach. The only difference will be that instead of keeping track of all nodes of a level, we will only track the running sum of the values of all nodes in each level. In the end, we will append the average of the current level to the result array.

````
class TreeNode {
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
  }
}

function findLevelAverages(root) {
  let result = []
  
  //edge case => no root
  if(!root) { 
    return result
  }
  
  const queue = [root]
  
  while(queue.length > 0) {
    let levelSize = queue.length
    let levelSum = 0.0
    
    for(let i = 0; i < levelSize; i++){
      let currentNode = queue.shift()
      
      //add the node's value to the running sum
      levelSum += currentNode.value
      
      //insert the children of the current node to the queue
      if(currentNode.left !== null) {
        queue.push(currentNode.left)
      }
      
      if(currentNode.right !== null) {
        queue.push(currentNode.right)
      }
    }
    
    //append the current level's average to the result array
    result.push(levelSum/levelSize)
  }
  return result
}

var root = new TreeNode(12)
root.left = new TreeNode(7)
root.right = new TreeNode(1)
root.left.left = new TreeNode(9)
root.left.right = new TreeNode(2)
root.right.left = new TreeNode(10)
root.right.right = new TreeNode(5)

console.log(`Level averages are: ${findLevelAverages(root)}`)
````
- The time complexity of the above algorithm is `O(N)`, where `N` is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
- The space complexity of the above algorithm will be `O(N)` which is required for the queue. Since we can have a maximum of `N/2` nodes at any level (this could happen only at the lowest level), therefore we will need `O(N)` space to store them in the queue

### Level Maximum in a Binary Tree 
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
> 🌟  Find the largest value on each level of a binary tree.

We will follow a similar approach, but instead of having a running sum we will track the maximum value of each level.

`maxValue = Math.max(maxValue, currentNode.val)`

## Minimum Depth of a Binary Tree (easy)
https://leetcode.com/problems/minimum-depth-of-binary-tree/

> Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the <b>shortest path from the root node to the nearest leaf node</b>.

This problem follows the <b>Binary Tree Level Order Traversal</b> pattern. We can follow the same <b>BFS</b> approach. The only difference will be, instead of keeping track of all the nodes in a level, we will only track the depth of the tree. As soon as we find our first leaf node, that level will represent the minimum depth of the tree.
````
class TreeNode {
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
  }
}

function findMinimumDepth(root) {
  //edge case => no root
  if(!root) {
    return 0
  }
  
  const queue = [root]
  
  let minimumTreeDepth = 0
  while(queue.length > 0) {
    minimumTreeDepth++
    let levelSize = queue.length
    
    for(let i = 0; i < levelSize; i++) {
      let currentNode = queue.shift()
      
      //check if this is a leaf node
      if(currentNode.left === null && currentNode.right === null) {
        return minimumTreeDepth
      }
      
      //insert the children of current node in the queue
      if(currentNode.left !== null) {
        queue.push(currentNode.left)
      }
      if(currentNode.right !== null) {
        queue.push(currentNode.right)
      }  
    }
  }  
}

const root = new TreeNode(12)
root.left = new TreeNode(7)
root.right = new TreeNode(1)
root.right.left = new TreeNode(10)
root.right.right = new TreeNode(5)
console.log(`Tree Minimum Depth: ${findMinimumDepth(root)}`)
root.left.left = new TreeNode(9)
root.right.left.left = new TreeNode(11)
console.log(`Tree Minimum Depth: ${findMinimumDepth(root)}`)
````
- The time complexity of the above algorithm is `O(N)`, where `N` is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
- The space complexity of the above algorithm will be `O(N)` which is required for the queue. Since we can have a maximum of `N/2` nodes at any level (this could happen only at the lowest level), therefore we will need `O(N)` space to store them in the queue.

### Maximum Depth of a Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
> Given a binary tree, find its maximum depth (or height).

We will follow a similar approach. Instead of returning as soon as we find a leaf node, we will keep traversing for all the levels, incrementing `maximumDepth` each time we complete a level. 
````
class TreeNode {
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
  }
}

function findMaximumDepth(root) {
  //edge case => no root
  if(!root) {
    return 0
  }
  
  const queue = [root]
  
  let maximumTreeDepth = 0
  
  while(queue.length > 0) {
    maximumTreeDepth++
    const levelSize = queue.length
    
    for(let i = 0; i < levelSize; i++) {
      let currentNode = queue.shift()
      
      //insert the children of current node in the queue
      if(currentNode.left !== null) {
        queue.push(currentNode.left)
      }
      if(currentNode.right !== null) {
        queue.push(currentNode.right)
      }  
    }
  }  
  return maximumTreeDepth
}

const root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
console.log(`Tree Maximum Depth: ${findMaximumDepth(root)}`);
root.left.left = new TreeNode(9);
root.right.left.left = new TreeNode(11);
console.log(`Tree Maximum Depth: ${findMaximumDepth(root)}`);
````
## Level Order Successor (easy) 😕
> Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.

This problem follows the <b>Binary Tree Level Order Traversal</b> pattern. We can follow the same <b>BFS</b> approach. The only difference will be that we will not keep track of all the levels. Instead we will keep inserting child nodes to the queue. As soon as we find the given node, we will return the next node from the queue as the level order successor.

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
    this.value = value
    this.left = null
    this.right = null
  }
}

function findSuccessor(root, key) {
  //edge case => no root
  // if(!root) {
  //   return null
  // }
 if (root === null) {
    return null;
  }

  const queue = new Deque();
  queue.addFront(root);
  while (queue.length > 0) {
    currentNode = queue.shift();
    // insert the children of current node in the queue
    if (currentNode.left !== null) {
      queue.push(currentNode.left);
    }
    if (currentNode.right !== null) {
      queue.push(currentNode.right);
    }
    // break if we have found the key
    if (currentNode.val === key) {
      break;
    }
  }

  if (queue.length > 0) {
    return queue.peek();
  }
  return null;
}

var root = new TreeNode(12)
root.left = new TreeNode(7)
root.right = new TreeNode(1)
root.left.left = new TreeNode(9)
root.right.left = new TreeNode(10)
root.right.right = new TreeNode(5)
result = findSuccessor(root, 12)
if (result != null)
  console.log(result.val)
result = findSuccessor(root, 9)
if (result != null)
  console.log(result.val)
````

- The time complexity of the above algorithm is `O(N)`, where `N` is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
- The space complexity of the above algorithm will be `O(N)` which is required for the queue. Since we can have a maximum of `N/2` nodes at any level (this could happen only at the lowest level), therefore we will need `O(N)` space to store them in the queue.

## 😕 Connect Level Order Siblings (medium)
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
> Given a binary tree, connect each node with its level order successor. The last node of each level should point to a `null` node.

This problem follows the <b>Binary Tree Level Order Traversal</b> pattern. We can follow the same <b>BFS</b> approach. The only difference is that while traversing a level we will remember the previous node to connect it with the current node.
````
class TreeNode {
  constructor(val) {
    this.val = val
    this.left = null
    this.right = null
    this.next = null
  }
}

  // level order traversal using 'next' pointer
 function printLevelOrder() {
    console.log("Level order traversal using 'next' pointer: ");
    let nextLevelRoot = this;
    while (nextLevelRoot !== null) {
      let currentNode = nextLevelRoot;
      nextLevelRoot = null;
      while (currentNode != null) {
        process.stdout.write(`${currentNode.val} `);
        if (nextLevelRoot === null) {
          if (currentNode.left !== null) {
            nextLevelRoot = currentNode.left;
          } else if (currentNode.right !== null) {
            nextLevelRoot = currentNode.right;
          }
        }
        currentNode = currentNode.next;
      }
      console.log();
    }
  }


function connectLevelOrderSiblings(root) {
  //if root is null return an empty array
  if(!root) return []
  
  //initilize the queue with root
  const queue = [root]
  
  // //declare output array
  // const levels = []
  
  while(queue.length > 0) {
    let previousNode = null
    
    //get length prior to dequeue
    const levelSize = queue.length
    
    // //declare this level
    // const currLevel = []
    
    //connect all nodes of this level
    for(let i = 0; i < levelSize; i++) {
      //get the next node
      const currentNode = queue.shift()
      if(previousNode !== null) {
        previousNode.next = currentNode
      }
      previousNode = currentNode
      
      //insert the children of currentNode in the queue
      if(currentNode.left !== null) {
        queue.push(currentNode.left)
      }
      if(currentNode.right !== null) {
        queue.push(currentNode.right)
      }
      
    //   //after we add left and right for current, we add to currLevel
    //   currLevel.push(current.val)
    }
    
    // //level has been finished. Push into output array
    // levels.push(currLevel)
  }
  // return levels
}

const root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);
connectLevelOrderSiblings(root);

printLevelOrder(root)
````
- The time complexity of the above algorithm is `O(N)`, where `‘N’` is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
- The space complexity of the above algorithm will be `O(N)`, which is required for the queue. Since we can have a maximum of `N/2`nodes at any level (this could happen only at the lowest level), therefore we will need `O(N)` space to store them in the queue.

## 🌟 Connect All Level Order Siblings (medium) 
## 🌟 Right View of a Binary Tree (easy) 
