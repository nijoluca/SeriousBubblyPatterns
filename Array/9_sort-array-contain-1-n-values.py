def sort_array(arr,n):
  for i in range(n-1):
    correct_pos=arr[i]-1
    if arr[i]!=arr[correct_pos]:
      arr[i],arr[correct_pos]=arr[correct_pos],arr[i]
  return arr
arr=[10, 7, 9, 2, 8, 3, 5, 4, 6, 1]
n=len(arr)
print(sort_array(arr,n))