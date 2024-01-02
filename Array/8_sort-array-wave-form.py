def SortToWave(arr,n):
  arr.sort()
  for i in range(0,n-1,2):
    arr[i],arr[i+1]=arr[i+1],arr[i]
  return arr


arr=[1, 2, 3, 4, 5, 6, 7,8]
output=SortToWave(arr,len(arr))
print(f"The array after sorting  to  wave form is {output}")
