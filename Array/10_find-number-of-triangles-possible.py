def find_number_of_triangles(arr,n):
  count=0
  for i in range(n):
    for j in range(i+1,n):
      for k in range(j+1,n):
        if (arr[i]+arr[j] > arr[k] and arr[i]+arr[k] > arr[j] and arr[k]+arr[j]>arr[i]):
          count+=1
  return count


arr = [10, 21, 22, 100, 101, 200, 300]
n=len(arr)
print(f"The total number triangel arrays is :{find_number_of_triangles(arr,n)}")