"""Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0};"""
def mover_zeros(arr):
  j=0
  for i in range(len(arr)):
    if arr[i] != 0:
      arr[j],arr[i] = arr[i],arr[j]
      j+=1
  return arr


arr= [1, 2, 0, 4, 3, 0, 5, 0]
print(mover_zeros(arr))
