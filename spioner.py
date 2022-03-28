T, N = list(map(int, input().split()))
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

distances = [abs(aList[i] - bList[i]) for i in range(len(aList))]

def isValidX(x):
    counter = 0
    for distance in distances:
        if distance <= x:
            counter += 1
        else:
            counter = 0
        if counter >= N:
            return False
    return True

def binarySearch(l, r):
    m = (l + r + 1) // 2
    if l == r:
        return l

    if isValidX(m):
        return binarySearch(m, r)
    
    else:
        return binarySearch(l, m-1)

print(binarySearch(0, max(distances) - 1))


