import sys
sys.stdin = open("1966_input.txt", "r")

T = int(input())
# 버블정렬
for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(len(num)-1, 0, -1):  # 뒤에서부터 거꾸로 비교
        for j in range(i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    result = ' '.join(map(str, num))
    print(f'#{test_case} {result}')