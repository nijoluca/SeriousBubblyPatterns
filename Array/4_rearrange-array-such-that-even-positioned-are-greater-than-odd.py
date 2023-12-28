def rearrange(arr,n):
  for i in range(0,n-1,2):
    print(i)
    if arr[i] > arr[i+1]:
      arr[i],arr[i+1]=arr[i+1],arr[i]
  return arr

arr=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(rearrange(arr,len(arr)))