def rearrange_array_arr_i(arr,n):
    arr.sort()
    for i in range(n):
        if i not in arr:
            arr[i]=-1
        else:
            arr[i]=i
    return arr


arr=[-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(rearrange_array_arr_i(arr,len(arr)))