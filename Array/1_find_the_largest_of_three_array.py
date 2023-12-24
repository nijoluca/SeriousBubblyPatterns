"""Input: arr[] = {10, 4, 3, 50, 23, 90}
Output: 90, 50, 23"""

import sys 
def print3Largest(arr,arr_size):
  first=second=third=-sys.maxsize
  for i in  range(0,arr_size):
    if arr[i]>first:
      third=second
      second=first
      first=arr[i]
    elif arr[i] > second:
      third=second
      second=arr[i]
    elif arr[i] > third:
      third=arr[i]
  print("The three largest elements are",first,second,third)
  return
arr=[12,13,1,10,34,1]
n=len(arr)
print3Largest(arr,n)