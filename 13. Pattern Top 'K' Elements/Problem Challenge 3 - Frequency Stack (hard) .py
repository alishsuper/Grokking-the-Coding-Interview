'''
Problem Challenge 3

Frequency Stack (hard) 
Design a class that simulates a Stack data structure, implementing the following two operations:

push(int num): Pushes the number ‘num’ on the stack.
pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.
Example:

After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)
 
1. pop() should return 2, as it is the most frequent number
2. Next pop() should return 1
3. Next pop() should return 2
'''


#mycode
from heapq import *

class FrequencyStack:
  def __init__(self):
    self.heap = []
    self.mapping= {}

  def push(self, num):
    # TODO: Write your code here
    self.mapping[num] = self.mapping.get(num, 0) + 1
    if num not in self.heap:
      heappush(self.heap,(-self.mapping[num],num))
    else:
      index = self.heap.index(num)
      if index == len(self.heap) -1:
        self.heap = self.heap[:index]
      else:
        self.heap = self.heap[0:index] + self.heap[index+1:]
      heappush(self.heap,(-mapping[num],num))

  def pop(self):
    freq, i = heappop(self.heap)
    if -freq > 1:
      heappush(self.heap,(-freq+1, i))
    return i


def main():
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()



#answer
from heapq import *


class Element:

  def __init__(self, number, frequency, sequenceNumber):
    self.number = number
    self.frequency = frequency
    self.sequenceNumber = sequenceNumber

  def __lt__(self, other):
    # higher frequency wins
    if self.frequency != other.frequency:
      return self.frequency > other.frequency
    # if both elements have same frequency, return the element that was pushed later
    return self.sequenceNumber > other.sequenceNumber


class FrequencyStack:
  sequenceNumber = 0
  maxHeap = []
  frequencyMap = {}

  def push(self, num):
    self.frequencyMap[num] = self.frequencyMap.get(num, 0) + 1
    heappush(self.maxHeap, Element(
      num, self.frequencyMap[num], self.sequenceNumber))
    self.sequenceNumber += 1

  def pop(self):
    num = heappop(self.maxHeap).number
    # decrement the frequency or remove if this is the last number
    if self.frequencyMap[num] > 1:
      self.frequencyMap[num] -= 1
    else:
      del self.frequencyMap[num]

    return num


def main():
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()



'''
Time complexity 
The time complexity of push() and pop() is O(logN) where ‘N’ is the current number of elements in the heap.

Space complexity 
We will need O(N) space for the heap and the map, so the overall space complexity of the algorithm is O(N).
'''