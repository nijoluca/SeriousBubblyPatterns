def leaders_in_an_array(arr,n):
  max_right=arr[n-1]
  output=[]
  output.append(max_right)
  for i in range(n-2,-1,-1):
    if arr[i] > max_right:
      max_right=arr[i]
      output.insert(0,max_right)
  return output


arr= [16, 17, 4, 3, 5, 2]
print(leaders_in_an_array(arr,len(arr)))
  