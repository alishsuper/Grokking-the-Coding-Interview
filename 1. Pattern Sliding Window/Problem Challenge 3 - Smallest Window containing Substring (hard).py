'''
Problem Challenge 3

Smallest Window containing Substring (hard) 
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:

Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".

Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
'''


#mycode
import math
def find_substring(str, pattern):
  # TODO: Write your code here
  p_dict={}
  s_dict={}
  result=""

  win_start, min_len = 0, math.inf

  for p in pattern:
    if p not in p_dict:
      p_dict[p] = 1
    else:
      p_dict[p] += 1

  for win_end in range(len(str)):
    if str[win_end] not in s_dict:
      s_dict[str[win_end]] = 1
    else:
      s_dict[str[win_end]] += 1
    
    print(s_dict)

    while set(p_dict.keys()).issubset(set(s_dict.keys())):
      if win_end-win_start+1 < min_len:
        min_len=win_end-win_start+1
        if win_end == len(str)-1:
          result=str[win_start:]
        else:
          result=str[win_start:win_end+1]

      if s_dict[str[win_start]] == 1:
        del s_dict[str[win_start]]
      else:
        s_dict[str[win_start]] -= 1
      win_start += 1

  return result



#answer
def find_substring(str, pattern):
  window_start, matched, substr_start = 0, 0, 0
  min_length = len(str) + 1
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # try to extend the range [window_start, window_end]
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in char_frequency:
      char_frequency[right_char] -= 1
      if char_frequency[right_char] >= 0:  # Count every matching of a character
        matched += 1

    # Shrink the window if we can, finish as soon as we remove a matched character
    while matched == len(pattern):
      if min_length > window_end - window_start + 1:
        min_length = window_end - window_start + 1
        substr_start = window_start

      left_char = str[window_start]
      window_start += 1
      if left_char in char_frequency:
        # Note that we could have redundant matching characters, therefore we'll decrement the
        # matched count only when a useful occurrence of a matched character is going out of the window
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  if min_length > len(str):
    return ""
  return str[substr_start:substr_start + min_length]


def main():
  print(find_substring("aabdec", "abc"))
  print(find_substring("abdabca", "abc"))
  print(find_substring("adcad", "abc"))

main()



'''
Time Complexity 
The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

Space Complexity 
The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap. 
In the worst case, we also need O(N) space for the resulting substring, which will happen when the input string is a permutation of the pattern.
'''