def mergearray(a1,a2):
  output=a1+a2
  output.sort()
  for i in range(len(a1)):
      a1[i]=output[i]
  for j in range(len(a2)):
      a2[j]=output[len(a1)+j]
  return a1,a2



a1=[1, 5, 9, 10, 15, 20]
a2=[2, 3, 8, 13]
print(mergearray(a1,a2))