# Pattern 14: K-way merge

The K-way Merge pattern looks like this;
- We can push the smallest (first) element of each sorted array in a Min Heap to get the overall minimum.
- After this step, we can take out the smallest (top) element from the heap and then add it to the merged list.
- After removing the smallest element from the heap, insert the next element of the same list into the heap.
- We can repeat steps 2 and 3 to populate the merged list in sorted order.

For this pattern,
Time Complexity = O(N log K) where N is the total number of elements in all the K input arrays.
Space Complexity = O(K)
## Ways to identify this pattern:
- For this kind of pattern, the problem will feature sorted arrays, lists, or a matrix
- The problem will ask us to merge sorted lists, find the smallest element in a sorted list.
