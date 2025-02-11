# https://www.acmicpc.net/problem/12927

arr = list(input())
N = len(arr)
# print(arr)
arr.insert(0, 'N')

count = 0
for i in range(1, N+1):
    if arr[i] == 'Y': # 'N'이면 넘어간다
        for x in range(i, N+1, i):  # i의배수
            if arr[x] == 'Y':
                arr[x] = 'N'
            else:
                arr[x] = 'Y'
        count += 1
if 'Y' in arr:   # 모든 전구를 끌 수 없는 경우
    print(-1)
else:
    print(count)
