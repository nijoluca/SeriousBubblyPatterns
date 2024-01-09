def kth_largest_sum_contiguous_subarray(arr,n,k):
  result=[]
  for i in range(n):
    sum=0
    for j in range(i,n):
      sum += arr[j]
      result.append(sum)

  result.sort(reverse=True)
  return result[k-1]

arr = [ 20, -5, -1]
n=len(arr)
k=3
print(kth_largest_sum_contiguous_subarray(arr,n,k))
    
  