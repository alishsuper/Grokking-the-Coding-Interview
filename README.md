# Grokking the Coding Interview in 16 Patterns

# Pattern 1: Sliding Window

They are subsets of dynamic programming problems, through the approach to solving them is quite different from the one in solving *tabulation* and *memoization* problems.

## How do you identify them ?

The first thing you want to be able to do is <u>identify a problem</u> that uses a sliding window paradigm.

Some giveaways:

1. The problem will <u>involve a data structure that is ordered and iterable</u> like an array or a string. 
2. You are looking for <u>some contiguous subrange in that array/string</u>, like a longest, shortest or target value, or whether a value is contained with the iterable.
3. There is an apparent naïve or <u>brute force solution that runs in O(N<sup>2</sup>), O(2<sup>N</sup>)</u> or some other large time complexity.

> The biggest giveaway is that the thing you are looking for is often some kind of **optimal**, like the **longest** sequence or **shortest** sequence of something that satisfies a given condition **exactly**.
>
> The thing about sliding window problems is that most of the time they <u>can be solved in O(N) time and O(1) space complexity</u>.

Example, **Bit-Flip Problem**

Given a binary array, find the maximum number of zeroes in an array with one flip of a subarray allowed. A flip operation switches all 0s to 1s and vice versa.

OR

You are given a binary string(*i.e.* with characters `0` and `1`) S consisting of characters S<sub>1</sub>, S<sub>2</sub>, …, S<sub>N</sub>. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters S<sub>L</sub>, S<sub>L+1</sub>, …, S<sub>R</sub>. By flipping, we mean change character `0` to `1` and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of `1`s is maximized. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

```
S = 010

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
```

## Abstract Idea

**Static Sliding Window**

![static-sliding-window](https://raw.githubusercontent.com/aditya109/Grokking-The-Coding-Interview/main/sliding-window/assets/sliding-window-abstract-idea.svg)

Dead Giveaways:

- max sum subarray of size `K`.

**Dynamically Resizable Window**

![](https://raw.githubusercontent.com/aditya109/Grokking-The-Coding-Interview/main/sliding-window/assets/dynamic-sliding-window.svg?token=AFH4ROZRN3JNX5CJCXIURXTACYUEU)

Dead giveaway:

- smallest sum >= some value `S`.

**Dynamic Variant w/ Auxiliary Data Structure**

Dead giveaway:

- Longest substring w/ no more than `k` distinct characters.
- String permutations.

### Example Problems
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

# Pattern 2: Two Pointer

## How do you identify ??

Two pointer technique is normally used for searching and it uses two pointer in one loop over the given data structure.

In order to use two pointers, most of the times the ***data structure needs to be ordered in some way***, which helps us to reduce the time complexity from **O(n<sup>2</sup>)** or **O(n<sup>3</sup>)** to **O(n)** of just one loop with two pointers and search each item just one time.

So depending on whether the input string is sorted or not, the two-pointer can take **O(n log n)** time complexity or even better which is **O(n)**.

## Types of two-pointers

1. **Opposite Directional**: One pointer starts from the beginning while the other pointer starts from the end. They move toward each other until they both meet or some condition satisfy.
   ![](https://raw.githubusercontent.com/aditya109/Grokking-The-Coding-Interview/main/two-pointers/assets/opposite-directional-2-pointers.svg)
   
   
   
2. **Equi-Directional**: Both start from the beginning, one slow-runner and the other is fast-runner.
   ![](https://raw.githubusercontent.com/aditya109/Grokking-The-Coding-Interview/main/two-pointers/assets/equi-directional-2-pointers.svg)

## Description

Given a sort array A, having N integers, find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X

```pseudocode
function isPairSum(A[], arrayLength, targetSum)
	startPointer := 0
	endPointer := arrayLength - 1
	
	while startPointer < endPointer
		if A[i] + A[j] == targetSum
			return True
		else if A[i] + A[j] < targetSum
			startPointer += 1
		else endPointer -= 1
	return False
```

Time Complexity: **O(N)**

- Pair with Target Sum (easy) https://leetcode.com/problems/two-sum/
- Remove Duplicates (easy) https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- Squaring a Sorted Array (easy) https://leetcode.com/problems/squares-of-a-sorted-array/
- Triplet Sum to Zero (medium) https://leetcode.com/problems/3sum/
- Triplet Sum Close to Target (medium) https://leetcode.com/problems/3sum-closest/
- Triplets with Smaller Sum (medium) https://leetcode.com/problems/3sum-smaller/
- Subarrays with Product Less than a Target (medium) https://leetcode.com/problems/subarray-product-less-than-k/
- Dutch National Flag Problem (medium) https://leetcode.com/problems/sort-colors/
- Problem Challenge 1 - Quadruple Sum to Target (medium) https://leetcode.com/problems/4sum/
- Problem Challenge 2 - Comparing Strings containing Backspaces (medium) https://leetcode.com/problems/backspace-string-compare/
- Problem Challenge 3 - Minimum Window Sort (medium) https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

## Pattern 3: Fast & Slow pointers

The <b>Fast & Slow</b> pointer approach, also known as the <b>Hare & Tortoise algorithm</b>, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

One of the famous problems solved using this technique was <b>Finding a cycle in a LinkedList</b>. Let’s jump onto this problem to understand the <b>Fast & Slow</b> pattern.

- LinkedList Cycle (easy) https://leetcode.com/problems/linked-list-cycle/
- Middle of the LinkedList (easy) https://leetcode.com/problems/middle-of-the-linked-list/
- Start of LinkedList Cycle (medium) https://leetcode.com/problems/linked-list-cycle-ii/
- Happy Number (medium) https://leetcode.com/problems/happy-number/
- Problem Challenge 1 - Palindrome LinkedList (medium) https://leetcode.com/problems/palindrome-linked-list/
- Problem Challenge 2 - Rearrange a LinkedList (medium) https://leetcode.com/problems/reorder-list/
- Problem Challenge 3 - Cycle in a Circular Array (hard) https://leetcode.com/problems/circular-array-loop/

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
