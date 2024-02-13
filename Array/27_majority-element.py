from collections import Counter 
def majority(A):
    majority=0
    output=Counter(A)
    for i,j in output.items():
        if len(A)//2 < j:
            majority=i
    if majority != 0:
        return majority
    else:
        return "No Majority Element"

A=[1, 1, 2, 1, 3, 5, 1]       
print(majority(A))