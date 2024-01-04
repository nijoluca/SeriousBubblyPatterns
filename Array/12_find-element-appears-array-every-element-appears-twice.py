def find_element_appears_twice(arr):
  for element in arr:
    if arr.count(element) == 1:
      return element
    

arr=[2, 3, 5, 4, 5, 3, 4]
print(find_element_appears_twice(arr))
    