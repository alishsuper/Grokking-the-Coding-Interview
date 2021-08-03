# Pattern 11: Modified Binary Search

As we know, whenever we are given a sorted <b>Array</b> or <b>LinkedList</b> or <b>Matrix</b>, and we are asked to find a certain element, the best algorithm we can use is the <b>Binary Search</b>.

## Order-agnostic Binary Search (easy)
https://leetcode.com/problems/binary-search/
> Given a sorted array of numbers, find if a given number `key` is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.
>
> Write a function to return the index of the `key` if it is present in the array, otherwise return `-1`.

To make things simple, let’s first solve this problem assuming that the input array is sorted in ascending order. Here are the set of steps for <b>Binary Search</b>:
1. Let’s assume `start` is pointing to the first index and `end` is pointing to the last index of the input array (let’s call it `arr`). This means:
````
    int start = 0;
    int end = arr.length - 1;
````
2. First, we will find the `middle` of `start` and `end`. An easy way to find the middle would be: <i>middle=(start+end)/2</i>.  The safest way to find the middle of two numbers without getting an overflow is as follows:
````
     middle  = start + (end-start)/2
`````
3. Next, we will see if the `key` is equal to the number at index `middle`. If it is equal we return `middle` as the required index.
4. If `key` is not equal to number at index middle, we have to check two things:
- If `key < arr[middle]`, then we can conclude that the `key` will be smaller than all the numbers after index `middle` as the array is sorted in the ascending order. Hence, we can reduce our search to `end = mid - 1`.
- If `key > arr[middle]`, then we can conclude that the `key` will be greater than all numbers before index `middle` as the array is sorted in the ascending order. Hence, we can reduce our search to `start = mid + 1`.
- We will repeat steps 2-4 with new ranges of `start` to `end`. If at any time `start` becomes greater than `end`, this means that we can’t find the `key` in the input array and we must return `-1`.

If the array is sorted in the descending order, we have to update the step 4 above as:
- If `key > arr[middle]`, then we can conclude that the `key` will be greater than all numbers after index `middle` as the array is sorted in the descending order. Hence, we can reduce our search to `end = mid - 1`.
- If `key < arr[middle]`, then we can conclude that the `key` will be smaller than all the numbers before index `middle` as the array is sorted in the descending order. Hence, we can reduce our search to `start = mid + 1`.
Finally, how can we figure out the sort order of the input array? We can compare the numbers pointed out by `start` and `end` index to find the sort order. If `arr[start] < arr[end]`, it means that the numbers are sorted in ascending order otherwise they are sorted in the descending order.
````
function binarySearch (arr, key) {
  let start = 0
  let end = arr.length -1
  
  //check to see if arr is sorted ascending or descending
  const isAscending = arr[start] < arr[end]
  
  while(start <= end) {
    //calculate the middle of the current range
    let middle = Math.floor(start + (end-start)/2)
    
    if(key === arr[middle]) {
      return middle
    }
    
    if(isAscending) {
      //ascending order
      if(key < arr[middle]) {
        //the key can be in the first half
        end = middle - 1
      } else {
        //key > arr[middle], so the key can be in the 
        //second half
        start = middle + 1
      }
    } 
    else {
      //descending order
      if(key > arr[middle]) {
        //the key can be in the first half
        end = middle -1
      } else {
        //key < arr[middle], the key can be in the 
        //second half
        start = middle + 1
      }
    }
  }
  
  // key not found
  return -1;
};

binarySearch([4, 6, 10], 10)//2
binarySearch([1, 2, 3, 4, 5, 6, 7], 5)//4
binarySearch([10, 6, 4], 10)//0
binarySearch([10, 6, 4], 4)//2
````
- Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be `O(logN)` where `N` is the total elements in the given array.
- The algorithm runs in constant space `O(1)`.
