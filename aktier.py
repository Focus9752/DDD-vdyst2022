from math import floor


N, T = list(map(int, input().split()))
prices = list(map(int, input().split()))

#Startindex, slutindex, penge tjent
combinations = []

for i in range(len(prices)):
    investment = (T // prices[i]) * prices[i]
    remainder = T % prices[i]
    for j in range(len(prices)):
        if j <= i:
            continue
        multiplier = prices[j] / prices[i]
        combinations.append((i,j,floor(multiplier * investment + remainder)))
    
sortedCombinations = sorted(combinations, key=lambda earnings: earnings[2])
print(sortedCombinations[len(sortedCombinations) - 1][2])



