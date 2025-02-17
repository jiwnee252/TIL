# https://www.acmicpc.net/problem/2309

height = [int(input()) for _ in range(9)]
# print(height)

for i in range(9):
    for j in range(i+1, 9):
        if sum(height) - height[i] - height[j] == 100 and i != j:
            h1, h2 = height[i], height[j]

height.remove(h1)
height.remove(h2)

# print(height)
for i in sorted(height):
    print(i)