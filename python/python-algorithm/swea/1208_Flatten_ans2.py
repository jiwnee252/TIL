import sys
sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))

    arr.sort()   # 정렬 한다
    for _ in range(dump):
        # if arr[-1] - arr[0] <= 1:
        #     break
        arr[0] += 1
        arr[-1] -= 1
        arr.sort()

    print(f'#{test_case} {arr[-1] - arr[0]}')