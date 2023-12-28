def maxminarray(arr,n):
  temp=[0]*n
  small,large=0,n-1
  flag=True
  for i in range(n):
    if flag is True:
      temp[i]=arr[large]
      large-=1
    else:
      temp[i]=arr[small]
      small += 1
    flag=bool(1-flag)
  return temp
arr=[1, 2, 3, 4, 5, 6, 7]
print(maxminarray(arr,len(arr)))