'''
Problem Statement 
Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Example 1:

1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5
'''

#mycode
from heapq import *

class MedianOfAStream:

  minHeap = []
  maxHeap = []

  def insert_num(self, num):
   # TODO: Write your code here
    if not self.minHeap or num <= -self.minHeap[0]:
      heappush(self.minHeap, -num)
    else:
      heappush(self.maxHeap, num)
    
    if len(self.minHeap) > len(self.maxHeap) + 1:
      heappush(self.maxHeap, -heappop(self.minHeap))
    elif len(self.minHeap) < len(self.maxHeap):
      heappush(self.minHeap,-heappop(self.maxHeap))


  def find_median(self):
    # TODO: Write your code here
    if len(self.maxHeap) == len(self.minHeap):
      return (self.maxHeap[0] - self.minHeap[0]) / 2
    else:
      return -self.minHeap[0]


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()



#answer
from heapq import *


class MedianOfAStream:

  maxHeap = []  # containing first half of numbers
  minHeap = []  # containing second half of numbers

  def insert_num(self, num):
    if not self.maxHeap or -self.maxHeap[0] >= num:
      heappush(self.maxHeap, -num)
    else:
      heappush(self.minHeap, num)

    # either both the heaps will have equal number of elements or max-heap will have one
    # more element than the min-heap
    if len(self.maxHeap) > len(self.minHeap) + 1:
      heappush(self.minHeap, -heappop(self.maxHeap))
    elif len(self.maxHeap) < len(self.minHeap):
      heappush(self.maxHeap, -heappop(self.minHeap))

  def find_median(self):
    if len(self.maxHeap) == len(self.minHeap):
      # we have even number of elements, take the average of middle two elements
      return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

    # because max-heap will have one more element than the min-heap
    return -self.maxHeap[0] / 1.0


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()




'''
Time complexity 
The time complexity of the insertNum() will be O(logN) due to the insertion in the heap. 
The time complexity of the findMedian() will be O(1) as we can find the median from the top elements of the heaps.

Space complexity 
The space complexity will be O(N) because, as at any time, we will be storing all the numbers.
'''