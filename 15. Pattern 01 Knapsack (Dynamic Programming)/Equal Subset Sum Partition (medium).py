'''
Problem Statement 
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

Example 2:

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
'''


#my Top-down code
def can_partition(num):
  # TODO: Write your code here
  s = sum(num)
  if s %2 == 1:
    return False
  dp = [[False for x in range(int(s/2) + 1)] for y in range(len(num))]
  return can_partition_recursive(dp, num, int(s / 2), 0)


def can_partition_recursive(dp, num, sum, currentIndex):
  if sum == 0:
    return True
  if len(num) == 0 or currentIndex >= len(num):
    return False
  if dp[currentIndex][sum]:
    return dp[currentIndex][sum]
  if num[currentIndex] <= sum:
    if can_partition_recursive(dp, num, sum-num[currentIndex], currentIndex+1):
      dp[currentIndex][sum] = True
      return dp[currentIndex][sum]
  
  dp[currentIndex][sum] = can_partition_recursive(dp, num, sum, currentIndex+1)
  return dp[currentIndex][sum]

  

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()



#my bottom-up code
def can_partition(num):
  # TODO: Write your code here
  s = sum(num)
  if s %2 == 1:
    return False
  dp = [[False for x in range(int(s/2) + 1)] for y in range(len(num))]
  
  for i in range(len(num)):
    dp[i][0] = True
  
  for i in range(0, int(s/2) + 1):
    if num[0] == i:
      dp[0][i] = True

  for i in range(1, len(num)):
    for n in range(1, int(s/2) + 1): 
      if num[i] <= n:
        w1 = dp[i-1][n-num[i]]
      w2 = dp[i-1][n]
      dp[i][n] = w2 or w1
  
  return dp[len(num)-1][int(s/2)]

  

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()


#my bottom-up code with O(len(num)) space complexity
def can_partition(num):
  # TODO: Write your code here
  s = sum(num)
  if s %2 == 1:
    return False
  dp = [False for x in range(int(s/2) + 1)] 
  dp[0] = True

  for i in range(1, int(s/2) + 1):
    if num[0] == i:
      dp[i] = True
  
  for i in range(1,len(num)):
    for n in range(int(s/2),-1,-1):
      w1 = dp[n]
      if num[i] <= n:
        w2 = dp[n-num[i]]
      dp[n] = w1 or w2
  
  return dp[int(s/2)]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()




#Basic Solution
def can_partition(num):
  s = sum(num)
  # if 's' is a an odd number, we can't have two subsets with equal sum
  if s % 2 != 0:
    return False

  return can_partition_recursive(num, s / 2, 0)


def can_partition_recursive(num, sum, currentIndex):
  # base check
  if sum == 0:
    return True

  n = len(num)
  if n == 0 or currentIndex >= n:
    return False

  # recursive call after choosing the number at the `currentIndex`
  # if the number at `currentIndex` exceeds the sum, we shouldn't process this
  if num[currentIndex] <= sum:
    if(can_partition_recursive(num, sum - num[currentIndex], currentIndex + 1)):
      return True

  # recursive call after excluding the number at the 'currentIndex'
  return can_partition_recursive(num, sum, currentIndex + 1)


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()


'''
Time and Space complexity 
The time complexity of the above algorithm is exponential O(2^n), where ‘n’ represents the total number. 
The space complexity is O(n), which will be used to store the recursion stack.
'''



#Top-down Dynamic Programming with Memorization
def can_partition(num):
  s = sum(num)

  # if 's' is a an odd number, we can't have two subsets with equal sum
  if s % 2 != 0:
    return False

  # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
  dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(num))]
  return True if can_partition_recursive(dp, num, int(s / 2), 0) == 1 else False


def can_partition_recursive(dp, num, sum, currentIndex):
  # base check
  if sum == 0:
    return 1

  n = len(num)
  if n == 0 or currentIndex >= n:
    return 0

  # if we have not already processed a similar problem
  if dp[currentIndex][sum] == -1:
    # recursive call after choosing the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    if num[currentIndex] <= sum:
      if can_partition_recursive(dp, num, sum - num[currentIndex], currentIndex + 1) == 1:
        dp[currentIndex][sum] = 1
        return 1

    # recursive call after excluding the number at the currentIndex
    dp[currentIndex][sum] = can_partition_recursive(
      dp, num, sum, currentIndex + 1)

  return dp[currentIndex][sum]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()


'''
Time and Space complexity 
The above algorithm has the time and space complexity of O(N*S), 
where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.
'''


#Bottom-up Dynamic Programming
def can_partition(num):
  s = sum(num)

  # if 's' is a an odd number, we can't have two subsets with same total
  if s % 2 != 0:
    return False

  # we are trying to find a subset of given numbers that has a total sum of 's/2'.
  s = int(s / 2)

  n = len(num)
  dp = [[False for x in range(s+1)] for y in range(n)]

  # populate the s=0 columns, as we can always for '0' sum with an empty set
  for i in range(0, n):
    dp[i][0] = True

  # with only one number, we can form a subset only when the required sum is
  # equal to its value
  for j in range(1, s+1):
    dp[0][j] = num[0] == j

  # process all subsets for all sums
  for i in range(1, n):
    for j in range(1, s+1):
      # if we can get the sum 'j' without the number at index 'i'
      if dp[i - 1][j]:
        dp[i][j] = dp[i - 1][j]
      elif j >= num[i]:  # else if we can find a subset to get the remaining sum
        dp[i][j] = dp[i - 1][j - num[i]]

  # the bottom-right corner will have our answer.
  return dp[n - 1][s]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()


'''
Time and Space complexity 
The above solution the has time and space complexity of O(N*S), 
where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.
'''





