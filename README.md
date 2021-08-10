# Grokking the Coding Interview in 16 Patterns

## Pattern 1: Sliding Window

In many problems dealing with an array (or a LinkedList), we are asked to find or calculate something among all the contiguous subarrays (or sublists) of a given size. For example, take a look at this problem:

> Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

Let’s understand this problem with a real input:

`Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5`

A brute-force algorithm will calculate the sum of every 5-element contiguous subarray of the given array and divide the sum by ‘5’ to find the average.

The efficient way to solve this problem would be to visualize each contiguous subarray as a sliding window of `‘5’` elements. This means that we will slide the window by one element when we move on to the next subarray. To reuse the sum from the previous subarray, we will subtract the element going out of the window and add the element now being included in the sliding window. This will save us from going through the whole subarray to find the sum and, as a result, the algorithm complexity will reduce to `O(N)`.

- Maximum Sum Subarray of Size K (easy) https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/
- Smallest Subarray with a given sum (easy) https://leetcode.com/problems/minimum-size-subarray-sum/
- Longest Substring with K Distinct Characters (medium) https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
- Fruits into Baskets (medium) https://leetcode.com/problems/fruit-into-baskets/
- No-repeat Substring (hard) * https://leetcode.com/problems/longest-substring-without-repeating-characters/
- Longest Substring with Same Letters after Replacement (hard) https://leetcode.com/problems/longest-repeating-character-replacement/
- Longest Subarray with Ones after Replacement (hard) * https://leetcode.com/problems/max-consecutive-ones-iii/
- Problem Challenge 1 - Permutation in a String (hard) * https://leetcode.com/problems/permutation-in-string/
- Problem Challenge 2 - String Anagrams (hard) https://leetcode.com/problems/find-all-anagrams-in-a-string/
- Problem Challenge 3 - Smallest Window containing Substring (hard) * https://leetcode.com/problems/minimum-window-substring/
- Problem Challenge 4 - Words Concatenation (hard) https://leetcode.com/problems/substring-with-concatenation-of-all-words/

## Pattern 2: Two Pointer

In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a subarray. For example, take a look at the following problem:

> Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

To solve this problem, we can consider each element one by one (pointed out by the first pointer) and iterate through the remaining elements (pointed out by the second pointer) to find a pair with the given sum. The time complexity of this algorithm will be `O(N^2)` where `‘N’` is the number of elements in the input array.

Given that the input array is sorted, an efficient way would be to start with one pointer in the beginning and another pointer at the end. At every step, we will see if the numbers pointed by the two pointers add up to the target sum. If they do not, we will do one of two things:
1. If the sum of the two numbers pointed by the two pointers is greater than the target sum, this means that we need a pair with a smaller sum. So, to try more pairs, we can decrement the end-pointer.
2. If the sum of the two numbers pointed by the two pointers is smaller than the target sum, this means that we need a pair with a larger sum. So, to try more pairs, we can increment the start-pointer.

- Pair with Target Sum (easy)
- Remove Duplicates (easy)
- Squaring a Sorted Array (easy)
- Triplet Sum to Zero (medium)
- Triplet Sum Close to Target (medium)
- Triplets with Smaller Sum (medium)
- Subarrays with Product Less than a Target (medium) *
- Problem Challenge 1 - Quadruple Sum to Target (medium) *
- Problem Challenge 2 - Comparing Strings containing Backspaces (medium)
- Problem Challenge 3 - Minimum Window Sort (medium) *

## Pattern 3: Fast & Slow pointers

The <b>Fast & Slow</b> pointer approach, also known as the <b>Hare & Tortoise algorithm</b>, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

One of the famous problems solved using this technique was <b>Finding a cycle in a LinkedList</b>. Let’s jump onto this problem to understand the <b>Fast & Slow</b> pattern.

- LinkedList Cycle (easy)
- Middle of the LinkedList (easy)
- Start of LinkedList Cycle (medium) *
- Happy Number (medium) * 
- Problem Challenge 1 - Palindrome LinkedList (medium) *
- Problem Challenge 2 - Rearrange a LinkedList (medium)
- Problem Challenge 3 - Cycle in a Circular Array (hard) *

## Pattern 4: Merge Intervals

This pattern describes an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals, we either need to find overlapping intervals or merge intervals if they overlap.

Given two intervals (`a` and `b`), there will be six different ways the two intervals can relate to each other:
1. `a` and `b`do not overlap
2. `a` and `b` overlap, `b` ends after `a`
3. `a` completely overlaps `b`
4. `a` and `b` overlap, `a` ends after `b`
5. `b` completly overlaps `a`
6. `a` and `b` do not overlap

Understanding the above six cases will help us in solving all intervals related problems.
![](mergeintervals.png)

- Merge Intervals (medium)
- Insert Interval (medium) *
- Intervals Intersection (medium)
- Conflicting Appointments (medium)
- Problem Challenge 1 - Minimum Meeting Rooms (hard) *
- Problem Challenge 2 - Maximum CPU Load (hard)
- Problem Challenge 3 - Employee Free Time (hard) *

## Pattern 5: Cyclic Sort

This pattern describes an interesting approach to deal with problems involving arrays containing numbers in a given range. For example, take the following problem:

>You are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means that some numbers will be missing. Find all the missing numbers.

To efficiently solve this problem, we can use the fact that the input array contains numbers in the range of `1` to `‘n’`. 
For example, to efficiently sort the array, we can try placing each number in its correct place, i.e., placing `‘1’` at index `‘0’`, placing `‘2’` at index `‘1’`, and so on. Once we are done with the sorting, we can iterate the array to find all indices that are missing the correct numbers. These will be our required numbers.

- Cyclic Sort (easy)
- Find the Missing Number (easy)
- Find all Missing Numbers (easy)
- Find the Duplicate Number (easy)
- Find all Duplicate Numbers (easy)
- Problem Challenge 1 - Find the Corrupt Pair (easy)
- Problem Challenge 2 - Find the Smallest Missing Positive Number (medium)
- Problem Challenge 3 - Find the First K Missing Positive Numbers (hard) *

## Pattern 6: In-place Reversal of a LinkedList

In a lot of problems, we are asked to reverse the links between a set of nodes of a <b>LinkedList</b>. Often, the constraint is that we need to do this in-place, i.e., using the existing node objects and without using extra memory.

<b>In-place Reversal of a LinkedList pattern</b> describes an efficient way to solve the above problem.

- Reverse a LinkedList (easy) 
- Reverse a Sub-list (medium) 
- Reverse every K-element Sub-list (medium) *
- Problem Challenge 1 - Reverse alternating K-element Sub-list (medium)
- Problem Challenge 2 - Rotate a LinkedList (medium)

## Pattern 7: Tree Breadth First Search
This pattern is based on the <b>Breadth First Search (BFS)</b> technique to traverse a tree.

Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. We will use a <b>Queue</b> to keep track of all the nodes of a level before we jump onto the next level. This also means that the space complexity of the algorithm will be `O(W)`, where `W` is the maximum number of nodes on any level.

- Binary Tree Level Order Traversal (easy)
- Reverse Level Order Traversal (easy) * 
- Zigzag Traversal (medium)
- Level Averages in a Binary Tree (easy)
- Minimum Depth of a Binary Tree (easy) 
- Level Order Successor (easy)
- Connect Level Order Siblings (medium)
- Problem Challenge 1 - Connect All Level Order Siblings (medium)
- Problem Challenge 2 - Right View of a Binary Tree (easy) 

## Pattern 8: Depth First Search (DFS)

This pattern is based on the <b>Depth First Search (DFS)</b> technique to traverse a tree.

We will be using recursion (or we can also use a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing. This also means that the space complexity of the algorithm will be `O(H)`, where `‘H’` is the maximum height of the tree.

- Binary Tree Path Sum (easy)
- All Paths for a Sum (medium) *
- Sum of Path Numbers (medium)
- Path With Given Sequence (medium) *
- Count Paths for a Sum (medium)
- Problem Challenge 1 - Tree Diameter (medium) *
- Problem Challenge 2 - Path with Maximum Sum (hard) *

## Pattern 9: Two Heaps

In many problems, where we are given a set of elements such that we can divide them into two parts. To solve the problem, we are interested in knowing the smallest element in one part and the biggest element in the other part. This pattern is an efficient approach to solve such problems.

This pattern uses two <b>Heaps</b> to solve these problems; A <b>Min Heap</b> to find the smallest element and a <b>Max Heap</b> to find the biggest element.

- Find the Median of a Number Stream (medium) 
- Sliding Window Median (hard) *
- Maximize Capital (hard) * 
- Problem Challenge 1 - Next Interval (hard) 

## Pattern 10: Subsets

A huge number of coding interview problems involve dealing with <b>Permutations</b> and <b>Combinations</b> of a given set of elements. This pattern describes an efficient <b>Breadth First Search (BFS)</b> approach to handle all these problems.

- Subsets (easy)
- Subsets With Duplicates (easy) *
- Permutations (medium) *
- String Permutations by changing case (medium)
- Balanced Parentheses (hard) *
- Unique Generalized Abbreviations (hard) * 
- Problem Challenge 1 - Evaluate Expression (hard) *
- Problem Challenge 2 - Structurally Unique Binary Search Trees (hard) *
- Problem Challenge 3 - Count of Structurally Unique Binary Search Trees (hard)

## Pattern 11: Modified Binary Search

As we know, whenever we are given a sorted <b>Array</b> or <b>LinkedList</b> or <b>Matrix</b>, and we are asked to find a certain element, the best algorithm we can use is the <b>Binary Search</b>.

- Order-agnostic Binary Search (easy)
- Ceiling of a Number (medium) *
- Next Letter (medium)
- Number Range (medium) *
- Search in a Sorted Infinite Array (medium) *
- Minimum Difference Element (medium)
- Bitonic Array Maximum (easy)
- Problem Challenge 1 - Search Bitonic Array (medium)
- Problem Challenge 2 - Search in Rotated Array (medium) * 
- Problem Challenge 3 - Rotation Count (medium) *

## Pattern 12: Bitwise XOR

<b>XOR</b> is a logical bitwise operator that returns `0` (false) if both bits are the same and returns `1` (true) otherwise. In other words, it only returns `1` if exactly one bit is set to `1` out of the two bits in comparison.

- Single Number (easy)
- Two Single Numbers (medium) *
- Complement of Base 10 Number (medium)
- Problem Challenge 1

## Pattern 13: Top 'K' Elements

Any problem that asks us to find the top/smallest/frequent ‘K’ elements among a given set falls under this pattern.

The best data structure that comes to mind to keep track of ‘K’ elements is Heap. This pattern will make use of the Heap to solve multiple problems dealing with ‘K’ elements at a time from a set of given elements.

- Top 'K' Numbers (easy)
- Kth Smallest Number (easy)
- 'K' Closest Points to the Origin (easy)
- Connect Ropes (easy) *
- Top 'K' Frequent Numbers (medium)
- Frequency Sort (medium) *
- Kth Largest Number in a Stream (medium)
- 'K' Closest Numbers (medium)
- Maximum Distinct Elements (medium)
- Sum of Elements (medium) 
- Rearrange String (hard)
- Problem Challenge 1 - Rearrange String K Distance Apart (hard) 
- Problem Challenge 2 - Scheduling Tasks (hard) *
- Problem Challenge 3 - Frequency Stack (hard) 

## Pattern 14: K-way merge

- Merge K Sorted Lists (medium) *
- Kth Smallest Number in M Sorted Lists (Medium) 
- Kth Smallest Number in a Sorted Matrix (Hard) *
- Smallest Number Range (Hard) *
- Problem Challenge 1 - K Pairs with Largest Sums (Hard) 

## 15. Pattern : 0/1 Knapsack (Dynamic Programming)
- 0/1 Knapsack (medium)
- Equal Subset Sum Partition (medium) *
- Subset Sum (medium)
- Minimum Subset Sum Difference (hard) *
- Problem Challenge 1 - Count of Subset Sum (hard) 
- Problem Challenge 2 - Target Sum (hard) 

## 16. Pattern: Topological Sort (Graph)
- Topological Sort (medium) *
- Tasks Scheduling (medium)
- Tasks Scheduling Order (medium)
- All Tasks Scheduling Orders (hard) *
- Alien Dictionary (hard) 
- Problem Challenge 1 - Reconstructing a Sequence (hard) *
- Problem Challenge 2 - Minimum Height Trees (hard) *

## 17. Miscellaneous
- Kth Smallest Number (hard) *
