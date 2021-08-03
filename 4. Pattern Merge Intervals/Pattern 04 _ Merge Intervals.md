# Pattern 4 : Merge Intervals
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

## Merge Intervals (medium)
https://leetcode.com/problems/merge-intervals/

> Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Our goal is to merge the intervals whenever they overlap. 
The diagram above clearly shows a merging approach. Our algorithm will look like this:

1. Sort the intervals on the start time to ensure `a.start <= b.start`
2. If `a` overlaps `b` (i.e. `b.start <= a.end`), we need to merge them into a new interval `c` such that:
````
    c.start = a.start
    c.end = max(a.end, b.end)
````
We will keep repeating the above two steps to merge `c` with the next interval if it overlaps with `c`.

````
class Interval {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }

  get_interval() {
    return "[" + this.start + ", " + this.end + "]";
  }
}

function merge (intervals) {
  if(intervals.length < 2) {
    return intervals
  }
  
  //sort the intervals on the start time
  intervals.sort((a,b) => a.start - b.start
                )
  const mergedIntervals = []
  
  let start = intervals[0].start
  let end = intervals[0].end
  
  for(let i = 1; i < intervals.length; i++) {
    const interval = intervals[i]
    if(interval.start <= end) {
      //overlapping intervals, adjust the end
      end = Math.max(interval.end, end)    
    } else {
      //non-overlapping intercal, add the precious interval and reset
      mergedIntervals.push(new Interval(start, end))
      start = interval.start
      end = interval.end
    }
  }
  //add the last interval
  mergedIntervals.push(new Interval(start, end))
  return mergedIntervals;
};

merged_intervals = merge([new Interval(1, 4), new Interval(2, 5), new Interval(7, 9)]);
result = "";
for(i=0; i < merged_intervals.length; i++) {
  result += merged_intervals[i].get_interval() + " ";
}
console.log(`Merged intervals: ${result}`)
//Output: [[1,5], [7,9]]
//Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].


merged_intervals = merge([new Interval(6, 7), new Interval(2, 4), new Interval(5, 9)]);
result = "";
for(i=0; i < merged_intervals.length; i++) {
  result += merged_intervals[i].get_interval() + " ";
}
console.log(`Merged intervals: ${result}`)
//Output: [[2,4], [5,9]]
//Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].


merged_intervals = merge([new Interval(1, 4), new Interval(2, 6), new Interval(3, 5)]);
result = "";
for(i=0; i < merged_intervals.length; i++) {
  result += merged_intervals[i].get_interval() + " ";
}
console.log(`Merged intervals: ${result}`)
//Output: [[1,6]]
//Explanation: Since all the given intervals overlap, we merged them into one.
````
OR 
````
function merge(intervals) {
    if(intervals.length < 2) return intervals
  //sort
  intervals.sort((a, b) => a[0] - b[0])
  for(let i = 1; i < intervals.length; i++) {
    let current = intervals[i]
    let previous = intervals[i-1]
    if(current[0] <= previous[1]) {
      intervals[i] =[previous[0], Math.max(previous[1], current[1])]
      intervals.splice(i-1, 1)
      i--
       }
  }
  return intervals
};
````

- The time complexity of the above algorithm is `O(N * logN)`, where `N` is the total number of intervals. We are iterating the intervals only once which will take `O(N)`, in the beginning though, since we need to sort the intervals, our algorithm will take `O(N * logN)`.
- The space complexity of the above algorithm will be `O(N)` as we need to return a list containing all the merged intervals. We will also need `O(N)` space for sorting

>  Given a set of intervals, find out if any two intervals overlap.

 We can follow the same approach as discussed above to find if any two intervals overlap.
 
 ## Insert Interval (medium)
 https://leetcode.com/problems/insert-interval/
 
 > Given a list of non-overlapping intervals sorted by their start time, <b>insert a given interval at the correct position</b> and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

If the given list was not sorted, we could have simply appended the new interval to it and used the `merge()` function from <b>Merge Intervals</b>. But since the given list is sorted, we should try to come up with a solution better than `O(N * logN)`

When inserting a new interval in a sorted list, we need to first find the correct index where the new interval can be placed. In other words, we need to skip all the intervals which end before the start of the new interval. So we can iterate through the given sorted listed of intervals and skip all the intervals with the following condition:
`intervals[i].end < newInterval.start`
Once we have found the correct place, we can follow an approach similar to <b>Merge Intervals</b> to insert and/or merge the new interval. Let’s call the new interval `a` and the first interval with the above condition `b`. There are five possibilities:

The diagram above clearly shows the merging approach. To handle all four merging scenarios, we need to do something like this:
````
    c.start = min(a.start, b.start)
    c.end = max(a.end, b.end)
````
Our overall algorithm will look like this:

1. Skip all intervals which end before the start of the new interval, i.e., skip all `intervals` with the following condition:
````
    intervals[i].end < newInterval.start
````
2. Let’s call the last interval `b` that does not satisfy the above condition. If `b` overlaps with the new interval (a) (i.e. `b.start <= a.end`), we need to merge them into a new interval `c`:
````
    c.start = min(a.start, b.start)
    c.end = max(a.end, b.end)
````
3. We will repeat the above two steps to merge `c` with the next overlapping interval.

````
class Interval {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }

  print_interval() {
    process.stdout.write(`[${this.start}, ${this.end}]`);
  }
}

function insert (intervals, newInterval) {
  let merged = [];
  let i = 0
  
  //skip and add to output all intervals that come before the newInterval
  while(i < intervals.length && intervals[i].end < newInterval.start) {
    merged.push(intervals[i])
    i++
  }
  
  // merge all intervals that overlap with newInterval
  while(i < intervals.length && intervals[i].start <= newInterval.end) {
    newInterval.start = Math.min(intervals[i].start, newInterval.start)
    newInterval.end = Math.max(intervals[i].end, newInterval.end)
    i++
  }
  
  //insert the newInterval
  merged.push(newInterval)
  
  //add all the remaining intervals to the output
  while(i < intervals.length) {
    merged.push(intervals[i])
    i++
  }
  return merged;
};

//Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
// Output: [[1,3], [4,7], [8,12]]
// Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
process.stdout.write('Intervals after inserting the new interval: ');
let result = insert([
  new Interval(1, 3),
  new Interval(5, 7),
  new Interval(8, 12),
], new Interval(4, 6));
for (i = 0; i < result.length; i++) {
  result[i].print_interval();
}
console.log();

// Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
// Output: [[1,3], [4,12]]
// Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
process.stdout.write('Intervals after inserting the new interval: ');
result = insert([
  new Interval(1, 3),
  new Interval(5, 7),
  new Interval(8, 12),
], new Interval(4, 10));
for (i = 0; i < result.length; i++) {
  result[i].print_interval();
}
console.log();

// Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
// Output: [[1,4], [5,7]]
// Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
process.stdout.write('Intervals after inserting the new interval: ');
result = insert([new Interval(2, 3),
  new Interval(5, 7),
], new Interval(1, 4));
for (i = 0; i < result.length; i++) {
  result[i].print_interval();
}
console.log();
````

OR 

````
function insert (intervals, newInterval) {
    let merged = []
    let i = 0
    
    //skip and add to output all intervals that come before the newInterval
    while(i < intervals.length && intervals[i][1] < newInterval[0]) {
        merged.push(intervals[i])
        i++
    }
    
    //merge all intervals that overlap with newInterval
    while(i < intervals.length && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(intervals[i][0], newInterval[0])
        newInterval[1] = Math.max(intervals[i][1], newInterval[1])
        i++
    }
    //insert the newInterval
    merged.push(newInterval)
    
    //add all the remaining intervals to the output
    while(i < intervals.length) {
        merged.push(intervals[i])
        i++
    }
    return merged
};
````

- As we are iterating through all the intervals only once, the time complexity of the above algorithm is `O(N)`, where `N` is the total number of intervals.
- The space complexity of the above algorithm will be `O(N)` as we need to return a list containing all the merged intervals.

## Intervals Intersection (medium)
https://leetcode.com/problems/interval-list-intersections/

> Given two lists of intervals, find the <b>intersection of these two lists</b>. Each list consists of <b>disjoint intervals sorted on their start time</b>.

This problem follows the <b>Merge Intervals</b> pattern. As we have discussed under <b>Insert Interval</b>, there are five overlapping possibilities between two intervals ‘a’ and ‘b’. A close observation will tell us that whenever the two intervals overlap, one of the interval’s start time lies within the other interval. This rule can help us identify if any two intervals overlap or not.

![](mergeintervals.png)

Now, if we have found that the two intervals overlap, how can we find the overlapped part?

Again from the above diagram, the overlapping interval will be equal to:

    start = max(a.start, b.start)
    end = min(a.end, b.end) 
That is, the highest start time and the lowest end time will be the overlapping interval.

So our algorithm will be to iterate through both the lists together to see if any two intervals overlap. If two intervals overlap, we will insert the overlapped part into a result list and move on to the next interval which is finishing early.
````
function merge(intervalA, intervalB) {
  let result = []
  let i = 0
  let j = 0
  
  while(i < intervalA.length && j < intervalB.length) {
    //check if intervals overlap and intervalA[i]'s start time
    //lies with the other intervalB[j]
    let aOverlapsB = intervalA[i][0] >= intervalB[j][0] && intervalA[i][0] <= intervalB[j][1]
    
    //check if intervals overlap and intervalA[j]'s start time lies with the other intervalB[i]
    let bOverlapsA = intervalB[j][0] >= intervalA[i][0] && intervalB[j][0] <= intervalA[i][1]
    
    //store the intersection part
    if(aOverlapsB || bOverlapsA) {
      result.push([Math.max(intervalA[i][0], intervalB[j][0]), Math.min(intervalA[i][1],intervalB[j][1])])
    }
    //move next from the intercal which is finishing first
    if(intervalA[i][1] < intervalB[j][1]) {
      i++
    } else {
      j++
    }
  }
  return result
}

merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])//[2, 3], [5, 6], [7, 7], The output list contains the common intervals between the two lists.
merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])//[5, 7], [9, 10], The output list contains the common intervals between the two lists.
````
- As we are iterating through both the lists once, the time complexity of the above algorithm is `O(N + M)`, where `‘N’` and `‘M’` are the total number of intervals in the input arrays respectively.
- Ignoring the space needed for the result list, the algorithm runs in constant space `O(1)`.
## Conflicting Appointments (medium)
https://leetcode.com/problems/meeting-rooms/

> Given an array of intervals representing ‘N’ appointments, find out if a person can <b>attend all the appointments</b>.

The problem follows the <b>Merge Intervals</b> pattern. We can sort all the intervals by start time and then check if any two intervals overlap. A person will not be able to attend all appointments if any two appointments overlap.
````
function canAttendAllAppointments(appointmentTimes) {
  //sort intervals by start time
  appointmentTimes.sort((a,b) => a[0] -b[0])
  
  //check if any two intervals overlap
  for(let i = 1; i < appointmentTimes.length; i++) {
    if(appointmentTimes[i][0] < appointmentTimes[i-1][1]) {
      //note that in the comparison above, it is < and not <=
      //while merging we needed <= comparison, as we will be merging the two 
      //intervals have conditions appointmentTimes[i][0] === appointmentTimes[i-1][1]
      //but such intervals don't represent conflicting appointments
      //as one starts right after the other
      return false
    }
  }
  return true
}

canAttendAllAppointments([[1,4], [2,5], [7,9]])//false, Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
canAttendAllAppointments([[6,7], [2,4], [8,12]])//true, None of the appointments overlap, therefore a person can attend all of them.
canAttendAllAppointments([[4,5], [2,3], [3,6]])//false, Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
````
- The time complexity of the above algorithm is `O(N*logN)`, where `‘N’` is the total number of appointments. Though we are iterating the intervals only once, our algorithm will take `O(N * logN)` since we need to sort them in the beginning.
- The space complexity of the above algorithm will be `O(N)`, which we need for sorting. 

> 🌟 Given a list of appointments, find all the conflicting appointments.

## 🌟 Minimum Meeting Rooms (hard) 
https://leetcode.com/problems/meeting-rooms-ii/
## 🌟 Maximum CPU Load (hard)
## 🌟 Employee Free Time (hard)
https://leetcode.com/problems/employee-free-time/
