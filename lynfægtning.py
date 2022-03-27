N = int(input())
f = list(map(int, input().split()))
g = list(map(int, input().split()))

fighters = [[i + 1, f[i], g[i], i] for i in range(len(f))]

lowestGFighter = [0,0,10**9,0]
secondLowestGFighter = [0,0,10**9,0]
highestGFighter = [0,0,0,0]
lowestFFighter = [0,10**9,0,0]
highestFFighter = [0,0,0,0]

for fighter in fighters:
    if fighter[2] < lowestGFighter[2]:
        lowestGFighter = fighter
    if fighter[2] > highestGFighter[2]:
        highestGFighter = fighter
    if fighter[1] < lowestFFighter[1]:
        lowestFFighter = fighter
    if fighter[1] > highestFFighter[1]:
        highestFFighter = fighter

if lowestGFighter == highestFFighter:
    for fighter in fighters:
        if fighter != lowestGFighter:
            if fighter[2] < secondLowestGFighter[2]:
                secondLowestGFighter = fighter

fights = []


if lowestGFighter == highestFFighter:
    while not secondLowestGFighter[3] == 0:
        fights.append([secondLowestGFighter[0],fighters[secondLowestGFighter[3] - 1][0]])
        fighters.remove(fighters[secondLowestGFighter[3] - 1])
        secondLowestGFighter[3] -= 1
        for fighter in fighters:
            if fighter[3] >= secondLowestGFighter[3] and fighter != secondLowestGFighter:
                fighter[3] -= 1
else:
    while not lowestGFighter[3] == 0:
        fights.append([lowestGFighter[0],fighters[lowestGFighter[3] - 1][0]])
        fighters.remove(fighters[lowestGFighter[3] - 1])
        lowestGFighter[3] -= 1
        for fighter in fighters:
            if fighter[3] >= lowestGFighter[3] and fighter != lowestGFighter:
                fighter[3] -= 1

while not highestFFighter[3] - 1 == 0 or highestFFighter[3] == 0:
    fights.append([highestFFighter[0], fighters[highestFFighter[3] - 1][0]])
    fighters.remove(fighters[highestFFighter[3] - 1])
    highestFFighter[3] -= 1

fights.append([highestFFighter[0], lowestGFighter[0]])

print(highestFFighter[2] * lowestGFighter[2])

for fight in fights:
    print(fight[0], fight[1])

