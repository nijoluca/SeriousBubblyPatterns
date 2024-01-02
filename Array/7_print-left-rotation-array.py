def NRotation(arr,n,k):
  temp=[]
  mod=k%n
  for i in range(n):
      temp.append(arr[(mod+i)%n])
  return temp

arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 2
Output=NRotation(arr,n,k)
print( f"The array after {k} rotation is {Output}")
