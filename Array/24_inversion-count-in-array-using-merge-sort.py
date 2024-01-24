#first solution with O(n)

def Inversion_array_count(arr,n):
  count=1
  for i in range(n):
    for j in range(i+1,n):
      if arr[i] > arr[j]:
        count+=1
  return count

arr=[1, 20, 6, 4, 5]
n=len(arr)
print(Inversion_array_count(arr,n))