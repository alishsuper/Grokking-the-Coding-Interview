'''
Problem Statement 
Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52" 

Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
'''

#mycode
def find_letter_case_string_permutations(str):
  
  # TODO: Write your code here
  permutations = []
  permutations.append(str)

  for i in range(len(str)):
    if str[i].isalpha():
      for j in range(len(permutations)):
        newPermutation = list(permutations[j])
        newPermutation[i] = newPermutation[i].swapcase()
        permutations.append(''.join(newPermutation))

  return permutations


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()


#answer
def find_letter_case_string_permutations(str):
  permutations = []
  permutations.append(str)
  # process every character of the string one by one
  for i in range(len(str)):
    if str[i].isalpha():  # only process characters, skip digits
      # we will take all existing permutations and change the letter case appropriately
      n = len(permutations)
      for j in range(n):
        chs = list(permutations[j])
        # if the current character is in upper case, change it to lower case or vice versa
        chs[i] = chs[i].swapcase()
        permutations.append(''.join(chs))

  return permutations


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()



'''
Time complexity 
Since we can have 2^N permutations at the most and while processing each permutation we convert it into a character array, 
the overall time complexity of the algorithm will be O(N*2^N).

Space complexity 
All the additional space used by our algorithm is for the output list. 
Since we can have a total of O(2^N) permutations, the space complexity of our algorithm is O(N*2^N).
'''