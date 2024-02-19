def TwoPointerSum(arr,x):
    i=0
    j=len(arr)-1
    while i < j:
        if arr[i]+arr[j]==x:
            return True,i,j
        elif arr[i] + arr[j] > x:
            j -= 1
        else:
            i +=1
    return False

arr=[10, 20, 35, 50, 75, 80]
x=65
print(TwoPointerSum(arr,x))