def reorder_array_uindex(arr,index):
  n=len(arr)
  result=[0]*n
  for i in range(n):
    result[index[i]]=arr[i]
  return result 



arr=[50, 40, 70, 60, 90]
index=[3,  0,  4,  1,  2]
print(reorder_array_uindex(arr,index))
    