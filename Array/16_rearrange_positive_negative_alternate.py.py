def rearrange_negative_num_array(arr,n):
  i=-1
  for j in range(n):
    if arr[j] < 0:
      i+=1
      arr[j],arr[i]=arr[i],arr[j]

  
  neg_index=0
  pos_index=i+1
  while(pos_index < n and neg_index < pos_index and
        arr[neg_index] < 0):
   

    arr[neg_index],arr[pos_index]=arr[pos_index],arr[neg_index]
    pos_index += 1
    neg_index += 2
  return arr



arr=[-1, 2, -3, 4, 5, 6, -7, 8, 9]
n=len(arr)
print(rearrange_negative_num_array(arr,n))