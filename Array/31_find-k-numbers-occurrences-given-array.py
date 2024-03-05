from collections import Counter

def most_elements(arr,k):
    counts=Counter(arr)
    most_freq=(reversed(counts.most_common(k)))
    output=','.join(str(x[0]) for x in most_freq)
    return  output



arr=[3, 1, 4, 4, 5, 2, 6, 1]
k=2
print(most_elements(arr,k))
