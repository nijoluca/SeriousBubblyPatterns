def bubblesort(arr):
  n=len(arr)
  for i in range(n):
    swapped=False
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
        swapped=True
    if (swapped == False):
      break
  return arr
arr=[64, 34, 25, 12, 22, 11, 90]
print(bubblesort(arr))