def longest_substring(s):
  last_index = {}
  start = 0
  max_length = 0

  for end in range(len(s)):
      if s[end] in last_index and start <= last_index[s[end]]:
          start = last_index[s[end]] + 1

      last_index[s[end]] = end
      max_length = max(max_length, end - start + 1)

  return max_length

# Example usage:
input_string = "abcabcbb"
result = longest_substring(input_string)
print(result)
