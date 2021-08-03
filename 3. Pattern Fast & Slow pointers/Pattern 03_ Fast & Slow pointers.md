# Pattern 3: Fast & Slow pointers

The <b>Fast & Slow</b> pointer approach, also known as the <b>Hare & Tortoise algorithm</b>, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

One of the famous problems solved using this technique was <b>Finding a cycle in a LinkedList</b>. Let’s jump onto this problem to understand the <b>Fast & Slow</b> pattern.

## LinkedList Cycle (easy)
https://leetcode.com/problems/linked-list-cycle/

> Given the head of a <b>Singly LinkedList</b>, write a function to determine if the LinkedList has a </b>cycle</b> in it or not.

Imagine two racers running in a circular racing track. If one racer is faster than the other, the faster racer is bound to catch up and cross the slower racer from behind. We can use this fact to devise an algorithm to determine if a LinkedList has a cycle in it or not.

Imagine we have a slow and a fast pointer to traverse the LinkedList. In each iteration, the slow pointer moves one step and the fast pointer moves two steps. This gives us two conclusions:
1. If the LinkedList doesn’t have a cycle in it, the fast pointer will reach the end of the LinkedList before the slow pointer to reveal that there is no cycle in the LinkedList.
2. The slow pointer will never be able to catch up to the fast pointer if there is no cycle in the LinkedList.

If the LinkedList has a cycle, the fast pointer enters the cycle first, followed by the slow pointer. After this, both pointers will keep moving in the cycle infinitely. If at any stage both of these pointers meet, we can conclude that the LinkedList has a cycle in it. Let’s analyze if it is possible for the two pointers to meet. When the fast pointer is approaching the slow pointer from behind we have two possibilities:
1. The fast pointer is one step behind the slow pointer.
2. The fast pointer is two steps behind the slow pointer.

All other distances between the fast and slow pointers will reduce to one of these two possibilities. Let’s analyze these scenarios, considering the fast pointer always moves first:
1. If the fast pointer is one step behind the slow pointer: The fast pointer moves two steps and the slow pointer moves one step, and they both meet.
2. If the fast pointer is two steps behind the slow pointer: The fast pointer moves two steps and the slow pointer moves one step. After the moves, the fast pointer will be one step behind the slow pointer, which reduces this scenario to the first scenario. This means that the two pointers will meet in the next iteration.

This concludes that the two pointers will definitely meet if the LinkedList has a cycle. 

````
class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next
  }
}

function hasCycle(head) {
  let slow = head
  let fast = head
  while(fast !== null && fast.next !== null) {
    fast = fast.next.next;
    slow = slow.next
    
    if(slow === fast) {
      //found the cycle
      return true
    }
  }
  return false
}

head = new Node(1)
head.next = new Node(2)
head.next.next = new Node(3)
head.next.next.next = new Node(4)
head.next.next.next.next = new Node(5)
head.next.next.next.next.next = new Node(6)
console.log(`LinkedList has cycle: ${hasCycle(head)}`)

head.next.next.next.next.next.next = head.next.next
console.log(`LinkedList has cycle: ${hasCycle(head)}`)

head.next.next.next.next.next.next = head.next.next.next
console.log(`LinkedList has cycle: ${hasCycle(head)}`)
````

- Once the slow pointer enters the cycle, the fast pointer will meet the slow pointer in the same loop. Therefore, the time complexity of our algorithm will be `O(N)` where `‘N’` is the total number of nodes in the LinkedList.
- The algorithm runs in constant space `O(1)`.

> Given the head of a LinkedList with a cycle, find the length of the cycle.

Once the fast and slow pointers meet, we can save the slow pointer and iterate the whole cycle with another pointer until we see the slow pointer again to find the length of the cycle.

````
class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next
  }
}

function findCycleLength(head) {
  let slow = head
  let fast = head
  
  while(fast !== null && fast.next !== null) {
    fast = fast.next.next;
    slow = slow.next
    
    if(slow === fast) {
      //found the cycle
      return calculateCycleLength(slow)
    }
  }
  return 0
}

function calculateCycleLength(slow) {
  let current = slow
  let cycleLength = 0
  
  while(true) {
    current = current.next
    cycleLength++
    if(current === slow) {
      break
    }
  }
  return cycleLength
}

head = new Node(1)
head.next = new Node(2)
head.next.next = new Node(3)
head.next.next.next = new Node(4)
head.next.next.next.next = new Node(5)
head.next.next.next.next.next = new Node(6)
console.log(`LinkedList has cycle length of: ${findCycleLength(head)}`)

head.next.next.next.next.next.next = head.next.next
console.log(`LinkedList has cycle length of: ${findCycleLength(head)}`)

head.next.next.next.next.next.next = head.next.next.next
console.log(`LinkedList has cycle length of: ${findCycleLength(head)}`)
````

- The above algorithm runs in `O(N)` time complexity and `O(1)` space complexity.

## Start of LinkedList Cycle (medium)
https://leetcode.com/problems/linked-list-cycle-ii/

> Given the head of a <b>Singly LinkedList</b> that contains a cycle, write a function to find the <b>starting node of the cycle</b>.

If we know the length of the <b>LinkedList</b> cycle, we can find the start of the cycle through the following steps:
1. Take two pointers. Let’s call them `pointer1` and `pointer2`.
2. Initialize both pointers to point to the start of the LinkedList.
3. We can find the length of the LinkedList cycle using the approach discussed in <b>LinkedList Cycle</b>. Let’s assume that the length of the cycle is ‘K’ nodes.
4. Move `pointer2` ahead by ‘K’ nodes.
5. Now, keep incrementing `pointer1` and `pointer2` until they both meet.
6. As `pointer2` is ‘K’ nodes ahead of `pointer1`, which means, `pointer2` must have completed one loop in the cycle when both pointers meet. Their meeting point will be the start of the cycle.
````
class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next
  }
}

function findCycleStart(head) {
  let cycleLength = 0
  let slow = head
  let fast = head
   while((fast !== null && fast.next !== null)){
     fast = fast.next.next
     slow = slow.next
     
     if(slow === fast) {
       //found the cycle
       cycleLength = calculateCycleLength(slow)
       break
     }
   }
  
  return findStart(head, cycleLength)
};


function calculateCycleLength(slow) {
  let current = slow
  let cycleLength = 0
  
  while(true) {
    current = current.next
    cycleLength++
    if(current === slow) {
      break
    }
  }
  return cycleLength
}

function findStart(head, cycleLength) {
  let pointer1 = head
  let pointer2 = head
  //move pointer2 ahead by cycleLength nodes
  while(cycleLength > 0) {
    pointer2 = pointer2.next
    cycleLength--
  }
  
  //increment both pointers until they meet at the start
  //of the cycle
  while(pointer1 !== pointer2) {
    pointer1 = pointer1.next
    pointer2 = pointer2.next
  }
  return pointer1
}

head = new Node(1)
head.next = new Node(2)
head.next.next = new Node(3)
head.next.next.next = new Node(4)
head.next.next.next.next = new Node(5)
head.next.next.next.next.next = new Node(6)

head.next.next.next.next.next.next = head.next.next
console.log(`LinkedList cycle start: ${findCycleStart(head).value}`)

head.next.next.next.next.next.next = head.next.next.next
console.log(`LinkedList cycle start: ${findCycleStart(head).value}`)

head.next.next.next.next.next.next = head
console.log(`LinkedList cycle start: ${findCycleStart(head).value}`)
````

- As we know, finding the cycle in a LinkedList with `‘N’` nodes and also finding the length of the cycle requires `O(N)`. Also, as we saw in the above algorithm, we will need `O(N)` to find the start of the cycle. Therefore, the overall time complexity of our algorithm will be `O(N)`.
- The algorithm runs in constant space `O(1)`.

## Happy Number (medium)
https://leetcode.com/problems/happy-number/

Any number will be called a happy number if, after repeatedly replacing it with a number equal to the <b>sum of the square of all of its digits, leads us to number ‘1’</b>. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

The process, defined above, to find out if a number is a happy number or not, always ends in a cycle. If the number is a happy number, the process will be stuck in a cycle on number ‘1,’ and if the number is not a happy number then the process will be stuck in a cycle with a set of numbers. As we saw in Example-2 while determining if ‘12’ is a happy number or not, our process will get stuck in a cycle with the following numbers: 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

We saw in the <b>LinkedList Cycle</b> problem that we can use the <b>Fast & Slow</b> pointers method to find a cycle among a set of elements. As we have described above, each number will definitely have a cycle. Therefore, we will use the same fast & slow pointer strategy to find the cycle and once the cycle is found, we will see if the cycle is stuck on number ‘1’ to find out if the number is happy or not.

````
function findHappyNumber(num) {
  let slow = num
  let fast = num
  
  while(true) {
    //move one step
    slow = findSquareSum(slow)
    //move two steps
    fast = findSquareSum(findSquareSum(fast))
    
    if(slow === fast) {
      //found the cycle
      break
    }
  }
  //see if the cycle is stuck on the number 1
  return slow === 1
}

function findSquareSum(num) {
  let sum = 0
  while(num > 0) {
    let digit = num % 10
    sum += digit * digit
    num = Math.floor(num / 10)
  }
  return sum
  
}
````
`findHappyNumber(23)//true`

`23` is a happy number, Here are the steps to find out that `23` is a happy number:
1. 2² + 3² = 4 + 9 = 13
2. 1² + 3² = 1 + 9 = 10
3. 1² + 0² = 1 + 0 = 1

`findHappyNumber(12)//false`

`12` is not a happy number, Here are the steps to find out that `12` is not a happy number:
1. 1²+2²= 1 + 4 = 5
2. 5² = 25
3. 2² + 5² = 4 + 25 = 29
4. 2² + 9² = 4 + 81 = 85
5. 8² + 5² = 64 + 25 = 89
6. 8² + 9² = 64 + 81 = 145
7. 1² + 4² + 5²= 1 + 16 + 25 = 42
8. 4² + 2² = 16 + 4 = 20
9. 2² + 0² = 4 + 0 = 4
10. 4²= 16
11. 1² + 6² = 1 + 36 = 37
12. 3² + 7² = 9 + 49 = 58
13. 5² + 8²= 25 + 64 = 89
Step ‘13’ leads us back to step ‘5’ as the number becomes equal to ‘89’, this means that we can never reach ‘1’, therefore, ‘12’ is not a happy number.

`findHappyNumber(19)//true`

`19` is a happy number, Here are the steps to find out that 19 is a happy number:
1. 1² + 9² = 82
2. 8² + 2² = 68
3. 6² + 8² = 100
4. 1² + 0² + 0² = 1

`findHappyNumber(2)//false`

`2` is not a happy number

- The time complexity of the algorithm is difficult to determine. However we know the fact that all unhappy numbers eventually get stuck in the cycle: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

This sequence behavior tells us two things:
1. If the number `N` is less than or equal to 1000, then we reach the cycle or ‘1’ in at most 1001 steps.
2. For `N > 1000`, suppose the number has `‘M’` digits and the next number is `‘N1’`. From the above Wikipedia link, we know that the sum of the squares of the digits of `‘N’` is at most 9²M, or `81M`(this will happen when all digits of `‘N’` are `‘9’`).

This means:
1. `N1 < 81M`
2. As we know `M = log(N+1)`
3. Therefore: `N1 < 81 * log(N+1) => N1 = O(logN)`
- This concludes that the above algorithm will have a time complexity of `O(logN)`.
- The algorithm runs in constant space `O(1)`.

## Middle of the LinkedList (easy)
https://leetcode.com/problems/middle-of-the-linked-list/
> Given the head of a <b>Singly LinkedList</b>, write a method to return the <b>middle node</b> of the LinkedList.
>
> If the total number of nodes in the LinkedList is even, return the second middle node.

One brute force strategy could be to first count the number of nodes in the LinkedList and then find the middle node in the second iteration. Can we do this in one iteration?

We can use the <b>Fast & Slow</b> pointers method such that the fast pointer is always twice the nodes ahead of the slow pointer. This way, when the fast pointer reaches the end of the LinkedList, the slow pointer will be pointing at the middle node.

````
class Node {
  constructor(value, next = null) {
    this.value = value
    this.next = next
  }
}

function findMiddleOfLinkedList(head) {
  let slow = head
  let fast = head
  
  while(fast !== null && fast.next !== null) {
    slow = slow.next
    fast = fast.next.next
  }
  return slow
}

head = new Node(1)
head.next = new Node(2)
head.next.next = new Node(3)
head.next.next.next = new Node(4)
head.next.next.next.next = new Node(5)

console.log(`Middle Node: ${findMiddleOfLinkedList(head).value}`)

head.next.next.next.next.next = new Node(6)
console.log(`Middle Node: ${findMiddleOfLinkedList(head).value}`)

head.next.next.next.next.next.next = new Node(7)
console.log(`Middle Node: ${findMiddleOfLinkedList(head).value}`)
`````
- The above algorithm will have a time complexity of `O(N)` where `‘N’` is the number of nodes in the LinkedList.
- The algorithm runs in constant space `O(1)`.

## 🌟 Palindrome LinkedList (medium)
https://leetcode.com/problems/palindrome-linked-list/
## 🌟 Rearrange a LinkedList (medium)
## 🌟 Cycle in a Circular Array (hard)

