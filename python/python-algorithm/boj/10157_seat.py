C, R = map(int, input().split())
# print(C, R)   # 공연장의 격자 크기 (C*R)
K = int(input())
# print(K)  # 어떤 관객의 대기번호

arr = [[0] * C for _ in range(R)]
print(arr)

for i in range(C):
    for j in range(R-1, -1, -1):
