n, a, b = list(map(int, input().split()))
xList = list(map(int, input().split()))
yList = list(map(int, input().split()))

for i in range(len(xList)):
    if xList[i] == yList[i]:
        del(xList[i])
        del(yList[i])



