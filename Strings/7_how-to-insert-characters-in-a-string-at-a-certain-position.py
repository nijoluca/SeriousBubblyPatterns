def InsertStar(str_input,chars):
  n=len(str_input)
  j=0
  ans=""
  for i in range(n):
      if (j < len(chars) and i==chars[j]):
          ans += "*"
          j += 1
      ans += str_input[i]
  return ans



str_input = "geeksforgeeks"
chars = [1, 5, 7, 9]
print(InsertStar(str_input,chars))