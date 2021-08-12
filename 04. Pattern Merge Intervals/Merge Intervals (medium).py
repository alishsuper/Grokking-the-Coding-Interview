'''

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
 
Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
'''

#mycode
from __future__ import print_function


class interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
  intervals.sort(key= lambda x:x.start)
  merged = []
  # TODO: Write your code here
  merged.append(intervals[0])
  for i in range(1,len(intervals)):
    curr=intervals[i]
    prev=merged.pop()
    if prev.start <= curr.start and prev.end >= curr.end:
      merged.append(prev)
    elif prev.start >= curr.start and prev.end <= curr.end:
      merged.append(curr)
    elif prev.start <= curr.start and prev.end >= curr.start:
      merged.append(interval(prev.start, curr.end))
    elif prev.start >= curr.start and prev.end <= curr.start:
      merged.append(interval(curr.start, prev.end))
    else:
      merged.append(prev)
      merged.append(curr)
  return merged



def main():
  print("Merged intervals: ", end='')
  for i in merge([interval(1, 4), interval(2, 5), interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([interval(6, 7), interval(2, 4), interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([interval(1, 4), interval(2, 6), interval(3, 5)]):
    i.print_interval()
  print()

main()


#answer
from __future__ import print_function


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
  if len(intervals) < 2:
    return intervals

  # sort the intervals on the start time
  intervals.sort(key=lambda x: x.start)

  mergedIntervals = []
  start = intervals[0].start
  end = intervals[0].end
  for i in range(1, len(intervals)):
    interval = intervals[i]
    if interval.start <= end:  # overlapping intervals, adjust the 'end'
      end = max(interval.end, end)
    else:  # non-overlapping interval, add the previous internval and reset
      mergedIntervals.append(Interval(start, end))
      start = interval.start
      end = interval.end

  # add the last interval
  mergedIntervals.append(Interval(start, end))
  return mergedIntervals


def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()


main()


'''
Time complexity 
The time complexity of the above algorithm is O(N * logN), where ‘N’ is the total number of intervals. 
We are iterating the intervals only once which will take O(N), in the beginning though, 
since we need to sort the intervals, our algorithm will take O(N * logN).

Space complexity 
The space complexity of the above algorithm will be O(N) as we need to return a list containing all the merged intervals. 
We will also need O(N) space for sorting. 
For Java, depending on its version, Collection.sort() either uses Merge sort or Timsort, and both these algorithms need O(N) space. 
Overall, our algorithm has a space complexity of O(N).
'''