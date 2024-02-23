def minOperations(arr,n,k):
  arr_max=max(arr)
  res=0
  for i in range(n):
    if ((arr_max - arr[i]) % k != 0):
      return -1
    else:
      res += (arr_max- arr[i])/k
  return int(res)

arr=[21, 33, 9, 45, 63]
n=len(arr)
k=6
print(minOperations(arr,n,k))