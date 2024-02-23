def find3sum(A,size,value):
  for i in range(0,size-2):
    for j in range(i+1,size-1):
      for k in range(j+1,size):
        if A[i]+A[j]+A[k]==value:
          print("Triplet is : ",A[i],A[j],A[k])
          return True
  return False


A = [1, 4, 45, 6, 10, 8]
size=len(A)
value=22

find3sum(A,size,value)