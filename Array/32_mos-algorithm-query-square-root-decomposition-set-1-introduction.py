def MOquery(arr,query):
  for i in query:
      L,R=i
      s=0
      for j in range(L,R+1):
          s += arr[j]
      print("For sum of ",i, "is",s)

arr=[1, 1, 2, 1, 3, 4, 5, 2, 8]
query= [[0, 4], [1, 3], [2, 4]]      
print(MOquery(arr,query))