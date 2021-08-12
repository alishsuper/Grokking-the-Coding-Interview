# Pattern 10: Subsets

A huge number of coding interview problems involve dealing with <b>Permutations</b> and <b>Combinations</b> of a given set of elements. This pattern describes an efficient <b>Breadth First Search (BFS)</b> approach to handle all these problems.

## Subsets (easy)
https://leetcode.com/problems/subsets/

> Given a set with distinct elements, find all of its distinct subsets.

To generate all subsets of the given set, we can use the <b>Breadth First Search (BFS)</b> approach. We can start with an empty set, iterate through all numbers one-by-one, and add them to existing sets to create new subsets.

Let’s take the example-2 mentioned above to go through each step of our algorithm:

Given set: `[1, 5, 3]`
1. Start with an empty set: `[[]]`
2. Add the first number `1` to all the existing subsets to create new subsets: `[[],`<b>`[1]`</b>`];`
3. Add the second number `5` to all the existing subsets: `[[], [1], `<b>`[5], [1,5]`</b>`]`;
4. Add the third number `3` to all the existing subsets: `[[], [1], [5], [1,5], `<b>`[3], [1,3], [5,3], [1,5,3]`</b>`]`.

Since the input set has distinct elements, the above steps will ensure that we will not have any duplicate subsets.
````
function findSubsets(nums) {
  let subsets = []
  
  //start by adding the empty subset
  subsets.push([])
  
  for(let i = 0; i < nums.length; i++) {
    let currentNumber = nums[i]
    //we will take all existing subsets and insert the current number in them to create new subsets
    const n = subsets.length
    
    for(let j = 0; j < n; j++) {
      //create a new subset from the existing subset and insert the current element to it?
      //clone the permutation?
      subsets.push([...subsets[j], nums[i]])
    }
  }
  return subsets
}

findSubsets([1, 5, 3])
findSubsets([1, 3])
````
- Since, in each step, the number of subsets doubles as we add each element to all the existing subsets, therefore, we will have a total of `O(2ᴺ)` subsets, where `‘N’` is the total number of elements in the input set. And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm will be `O(N*2ᴺ)`.
- All the additional space used by our algorithm is for the output list. Since we will have a total of `O(2ᴺ)` subsets, and each subset can take up to `O(N)` space, therefore, the space complexity of our algorithm will be `O(N*2ᴺ)`.

## Subsets With Duplicates (medium)
https://leetcode.com/problems/subsets-ii/

> Given a set of numbers that might contain duplicates, find all of its distinct subsets.

This problem follows the <b>Subsets</b> pattern and we can follow a similar <b>Breadth First Search (BFS)</b> approach. The only additional thing we need to do is handle duplicates. Since the given set can have duplicate numbers, if we follow the same approach discussed in <b>Subsets</b>, we will end up with duplicate subsets, which is not acceptable. To handle this, we will do two extra things:
1. Sort all numbers of the given set. This will ensure that all duplicate numbers are next to each other.
2. Follow the same <b>BFS</b> approach but whenever we are about to process a duplicate (i.e., when the current and the previous numbers are same), instead of adding the current number (which is a duplicate) to all the existing subsets, only add it to the subsets which were created in the previous step.

Let’s take first Example mentioned below to go through each step of our algorithm:
````
Given set: [1, 5, 3, 3]  
Sorted set: [1, 3, 3, 5]
````
1. Start with an empty set: `[[]]`
2. Add the first number `1` to all the existing subsets to create new subsets: `[[], [1]]`;
3. Add the second number `3` to all the existing subsets: `[[], [1], [3], [1,3]]`.
4. The next number `3` is a duplicate. If we add it to all existing subsets we will get:
    ````
    [[], [1], [3], [1,3], [3], [1,3], [3,3], [1,3,3]]
    ````
````
We got two duplicate subsets: [3], [1,3]  
Whereas we only needed the new subsets: [3,3], [1,3,3] 
````
To handle this instead of adding `3` to all the existing subsets, we only add it to the new subsets which were created in the previous <b>3rd</b> step:
````
    [[], [1], [3], [1,3], [3,3], [1,3,3]]
````
5. Finally, add the forth number `5` to all the existing subsets: `[[], [1], [3], [1,3], [3,3], [1,3,3], [5], [1,5], [3,5], [1,3,5], [3,3,5], [1,3,3,5]]`

````
function subsetsWithDupe(nums) {
  let subsets = []
  nums.sort((a, b) => a-b)
  
  //start by adding the empty subset
  subsets.push([])
  
  let start = 0
  let end = 0
  
  for(let i = 0; i < nums.length; i++) {
    //if the current and previous elements are the same, 
    //create new subsets only from the subsets added in the previous step
   
    end = subsets.length
    
    for(let j = start; j < end; j++) {
      //create a new subset from the existing subset and add the current element to it
      subsets.push([...subsets[j], nums[i]])
      
      if(nums[i + 1] === nums[i]) {
        start = end
      } else {
        start = 0
      }
    }
  }
  return subsets
}

subsetsWithDupe([1, 5, 3, 3])
subsetsWithDupe([1, 3, 3])
````
- Since, in each step, the number of subsets doubles (if not duplicate) as we add each element to all the existing subsets, therefore, we will have a total of `O(2ᴺ)` subsets, where `‘N’` is the total number of elements in the input set. And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm will be `O(N*2ᴺ)`.
- All the additional space used by our algorithm is for the output list. Since, at most, we will have a total of `O(2ᴺ)` subsets, and each subset can take up to `O(N)` space, therefore, the space complexity of our algorithm will be `O(N*2ᴺ)`.
## Permutations (medium)
https://leetcode.com/problems/permutations/

> Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, `{1, 2, 3}` has the following six permutations:
1. `{1, 2, 3}`
2. `{1, 3, 2}`
3. `{2, 1, 3}`
4. `{2, 3, 1}`
5. `{3, 1, 2}`
6. `{3, 2, 1}`

If a set has `‘n’` distinct elements it will have `n!` permutations.

This problem follows the <b>Subsets</b> pattern and we can follow a similar <b>Breadth First Search (BFS)</b> approach. However, unlike <b>Subsets</b>, every permutation must contain all the numbers.

Let’s take the example mentioned below to generate all the permutations. Following a <b>BFS</b> approach, we will consider one number at a time:
1. If the given set is empty then we have only an empty permutation set: `[]`
2. Let’s add the first element `1`, the permutations will be: `[1]`
3. Let’s add the second element `3`, the permutations will be: `[3,1], [1,3]`
4. Let’s add the third element `5`, the permutations will be: `[5,3,1], [3,5,1], [3,1,5], [5,1,3], [1,5,3], [1,3,5]`
 
Let’s analyze the permutations in the 3rd and 4th step. How can we generate permutations in the 4th step from the permutations of the 3rd step?

If we look closely, we will realize that when we add a new number `5`, we take each permutation of the previous step and insert the new number in every position to generate the new permutations. For example, inserting `5` in different positions of `[3,1]` will give us the following permutations:
1. Inserting `5` before `3`: `[5,3,1]`
2. Inserting `5` between `3` and `1`: `[3,5,1]`
3. Inserting `5` after `1`: `[3,1,5]`

````
function findPermutations(nums) {
  let result = []
  let permutations = [[]]
  let numsLength = nums.length
  
  for(let i = 0; i < nums.length; i++) {
    const currentNumber = nums[i]
    
    //we will take all existing permutations and add the
    //current number to create a new permutation
    const n = permutations.length
    
    for(let p = 0; p < n; p++) {
      const oldPermutation = permutations.shift()
      
      
      //create a new permustion by adding the current number at every position
      for(let j = 0; j < oldPermutation.length + 1; j++) {
      
        //clone the permutation
        const newPermutation = oldPermutation.slice(0)
        
        //insert the current number at index j
        newPermutation.splice(j, 0, currentNumber)
        
        if(newPermutation.length === numsLength) {
          result.push(newPermutation)
        } else {
          permutations.push(newPermutation)
        }
      } 
    }  
  }
  
  return result
}


findPermutations([1, 3, 5])
````

- We know that there are a total of `N!` permutations of a set with `‘N’` numbers. In the algorithm above, we are iterating through all of these permutations with the help of the two ‘for’ loops. In each iteration, we go through all the current permutations to insert a new number in them. To insert a number into a permutation of size ‘`N’` will take `O(N)`, which makes the overall time complexity of our algorithm `O(N*N!)`.
- All the additional space used by our algorithm is for the `result` list and the `queue` to store the intermediate permutations. If you see closely, at any time, we don’t have more than `N!` permutations between the result list and the queue. Therefore the overall space complexity to store `N!` permutations each containing `N` elements will be `O(N*N!)`.

### Recursive Solution
## String Permutations by changing case (medium)
## Balanced Parentheses (hard)
https://leetcode.com/problems/generate-parentheses/
## Unique Generalized Abbreviations (hard)
https://leetcode.com/problems/generalized-abbreviation/
## 🌟 Evaluate Expression (hard)
https://leetcode.com/problems/different-ways-to-add-parentheses/
## 🌟 Structurally Unique Binary Search Trees (hard)
https://leetcode.com/problems/unique-binary-search-trees-ii/
## 🌟 Count of Structurally Unique Binary Search Trees (hard)
https://leetcode.com/problems/unique-binary-search-trees/
