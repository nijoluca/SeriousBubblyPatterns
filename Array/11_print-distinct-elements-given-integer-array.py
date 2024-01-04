def print_distinct_elements(arr):
  output=[]

  for element in arr:
      if arr.count(element) == 1:
        output.append(element)
  return output


arr = [1, 2, 3, 4, 5, 5, 7, 7, 8, 8, 9]

print(print_distinct_elements(arr))