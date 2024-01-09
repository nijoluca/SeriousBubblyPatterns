def find_subarray_with_given_sum(arr,target):
  current_sum=0
  start_index=0
  for index,i in enumerate(arr):
    current_sum += i

    while current_sum > target:
      current_sum -= arr[start_index]
      start_index+=1

    if current_sum == target:
      return arr[start_index:index+1]
  return None



arr = [1, 4, 20, 3, 10, 5]

target = 33
result = find_subarray_with_given_sum(arr,target)
print(result)
