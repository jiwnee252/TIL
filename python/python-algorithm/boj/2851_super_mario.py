mushrooms = []

score = 0

for i in range(10):
    mushrooms.append(int(input()))
# print(mushrooms)

for k in mushrooms:
    score += k
    if score >= 100:
        if score - 100 > 100 - score + k:
            score = score - k
        break

print(score)