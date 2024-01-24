def arraysort_012(arr):
  ones=[]
  twos=[]
  zeros=[]
  for i in range(len(arr)):
      if arr[i] == 0:
          zeros.append(arr[i])
      elif arr[i] == 1:
          ones.append(arr[i])
      else:
          twos.append(arr[i])
  return zeros+ones+twos

arr=[0,1,0,2,1,0]

print(arraysort_012(arr))