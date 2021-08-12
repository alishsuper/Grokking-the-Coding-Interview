'''
Problem Challenge 4

Words Concatenation (hard) 
Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
'''

#mycode
def find_word_concatenation(str, words):
  result_indices = []
  word_count = len(words)
  word_len=len(words[0])

  for i in range(len(str)-word_count*word_len+1):
    cnt = 0
    curr=str[i:i+word_count*word_len]
    
    for j in range(word_count):
      
      if words[j] not in curr:
        break
      else:
        cnt += 1
    
    if cnt== word_count:
      result_indices.append(i)
      
  return result_indices



#answer
def find_word_concatenation(str, words):
  if len(words) == 0 or len(words[0]) == 0:
    return []

  word_frequency = {}

  for word in words:
    if word not in word_frequency:
      word_frequency[word] = 0
    word_frequency[word] += 1

  result_indices = []
  words_count = len(words)
  word_length = len(words[0])

  for i in range((len(str) - words_count * word_length)+1):
    words_seen = {}
    for j in range(0, words_count):
      next_word_index = i + j * word_length
      # Get the next word from the string
      word = str[next_word_index: next_word_index + word_length]
      if word not in word_frequency:  # Break if we don't need this word
        break

      # Add the word to the 'words_seen' map
      if word not in words_seen:
        words_seen[word] = 0
      words_seen[word] += 1

      # No need to process further if the word has higher frequency than required
      if words_seen[word] > word_frequency.get(word, 0):
        break

      if j + 1 == words_count:  # Store index if we have found all the words
        result_indices.append(i)

  return result_indices


def main():
  print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
  print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()


'''
Time Complexity 
The time complexity of the above algorithm will be O(N * M * Len) where ‘N’ is the number of characters in the given string, 
‘M’ is the total number of words, and ‘Len’ is the length of a word.

Space Complexity 
The space complexity of the algorithm is O(M) since at most, we will be storing all the words in the two HashMaps. 
In the worst case, we also need O(N) space for the resulting list. So, the overall space complexity of the algorithm will be O(M+N).
'''