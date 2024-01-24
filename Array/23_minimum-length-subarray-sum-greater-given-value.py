def minimum_legth_of_array(arr,target):
  start=0
  end=0
  n=len(arr)
  min_len=float('inf')
  current_sum=0
  while end < n:
    while current_sum <= target and end < n:
      current_sum += arr[end]
      end+=1
    while current_sum > target and start  < n:
      min_len=min(min_len,end-start)
      current_sum -= arr[start]
      start += 1
  return min_len if min_len !=  float('inf') else 0
      
arr=[1, 4, 45, 6, 0, 19]    
target=51
result=minimum_legth_of_array(arr,target)
print(result)