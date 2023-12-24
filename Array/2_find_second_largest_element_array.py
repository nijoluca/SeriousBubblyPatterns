import sys
def SecondLargest(arr,n):
  second=first=-sys.maxsize
  if n < 2:
    print("Minimum size of array should be 2")
    return
  for i in range(0,n):
    if arr[i] > first:
      second=first
      first=arr[i]
    elif (arr[i] > second and arr[i] != first):
      second=arr[i]
  return second

arr=[12,35, 1, 10, 34, 1]
n=len(arr)
print(SecondLargest(arr,n))


"""Time complexity = O(n)
and space complexity = O(1)"""
