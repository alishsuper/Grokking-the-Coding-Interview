'''
Problem Statement 
Given an array of points in the a 2D2D plane, find ‘K’ closest points to the origin.

Example 1:

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
Example 2:

Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
Output: [[1, 3], [2, -1]]
'''

import math
from heapq import *

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')
    print(self.x **2+self.y **2 )
  def __lt__(self, other):
        
        return (self.x **2+self.y **2 ) > (other.x **2+other.y **2)

def find_closest_points(points, k):
  result = []
  # TODO: Write your code here
  for point in points:
    if len(result) <k:
      heappush(result, point)
    else:
      if (point.x **2+point.y **2 ) < (result[0].x **2+result[0].y **2):
        heappop(result)
        heappush(result, point)
  
  return result


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()



#answer
from __future__ import print_function
from heapq import *


class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  # used for max-heap
  def __lt__(self, other):
    return self.distance_from_origin() > other.distance_from_origin()

  def distance_from_origin(self):
    # ignoring sqrt to calculate the distance
    return (self.x * self.x) + (self.y * self.y)

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
  maxHeap = []
  # put first 'k' points in the max heap
  for i in range(k):
    heappush(maxHeap, points[i])

  # go through the remaining points of the input array, if a point is closer to the origin than the top point
  # of the max-heap, remove the top point from heap and add the point from the input array
  for i in range(k, len(points)):
    if points[i].distance_from_origin() < maxHeap[0].distance_from_origin():
      heappop(maxHeap)
      heappush(maxHeap, points[i])

  # the heap has 'k' points closest to the origin, return them in a list
  return list(maxHeap)


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()



'''
Time complexity 
The time complexity of this algorithm is (N*logK) as we iterating all points and pushing them into the heap.

Space complexity 
The space complexity will be O(K) because we need to store ‘K’ point in the heap.
'''