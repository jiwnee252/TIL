def preorder(k):
    if k:
        result.append(k)
        preorder(left[k])
        preorder(right[k])


N = int(input())
E = N - 1
arr = list(map(int, input().split()))
left = [0] * (N + 1)
right = [0] * (N + 1)
result = []

for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

preorder(1)
# print(result)

print(' '.join(map(str, result)))

'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
