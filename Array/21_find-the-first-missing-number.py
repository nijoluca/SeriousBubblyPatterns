def smallest_first_missingnum_array(arr,n):
  for i in range(n):
    if arr[i] != i:
      return i

  return n

arr= [0, 1, 2, 3, 4, 6, 7, 8]
n=len(arr)
print(smallest_first_missingnum_array(arr,n))








