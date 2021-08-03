'''
Problem Statement 
Any number will be called a happy number if, 
after repeatedly replacing it with a number equal to the sum of the square of all of its digits, 
leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. 
Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
'''

#mycode
def find_happy_number(num):
  # TODO: Write your code here
  fast, slow = num, num
  while True:
    fast = square(square(fast))
    slow = square(slow)

    if fast == slow:
      break

  return slow == 1

def square(num):
  square_num = 0
  while num  > 0:
    square_num += (num % 10) ** 2
    num = num // 10
  return square_num


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()


'''
Time Complexity #
The time complexity of the algorithm is difficult to determine. 
However we know the fact that all unhappy numbers eventually get stuck in the cycle: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

This sequence behavior tells us two things:
1. If the number NN is less than or equal to 1000, then we reach the cycle or ‘1’ in at most 1001 steps.
2. For N > 1000, suppose the number has ‘M’ digits and the next number is ‘N1’. 
From the above Wikipedia link, we know that the sum of the squares of the digits of ‘N’ is at most 9^2 M, or 81M 
(this will happen when all digits of ‘N’ are ‘9’).

This means:
1. N1 < 81M
2. As we know M = log(N+1)M=log(N+1)
3. Therefore: N1 < 81 * log(N+1)N1<81∗log(N+1) => N1 = O(logN)N1=O(logN)
This concludes that the above algorithm will have a time complexity of O(logN)O(logN).

Space Complexity 
The algorithm runs in constant space O(1)O(1).
'''