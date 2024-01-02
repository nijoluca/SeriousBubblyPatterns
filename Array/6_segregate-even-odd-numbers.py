def evenodd(arr,n):
  i=-1
  j=0
  while j<n:
    if arr[j]%2==0:
      i+=1
      arr[i],arr[j]=arr[j],arr[i]
    j+=1
  return arr

arr=[1, 3, 2, 4, 7, 6, 9, 10]
print(evenodd(arr,len(arr)))