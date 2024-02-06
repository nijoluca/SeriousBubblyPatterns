s = "GeeksforGeeks"
n=len(s)       
def leftRotation(s,d):
    return s[d:]+s[0:d]


def rightrotation(s,d):
    return leftRotation(s,len(s)-d)


s = "GeeksforGeeks"
d=2
print(leftRotation(s,d))
print(rightrotation(s,d))