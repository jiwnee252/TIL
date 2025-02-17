import sys
sys.stdin = open("1210.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(100)]

    def ladder(T):
        for j in range(100):
            if arr[99][j] == 2:
                i, j = 99, j
                break  # 2의위치 찾으면 종료

        while i > 0:  # 맨 위로 올라갈때까지 반복
            if j - 1 >= 0 and arr[i][j - 1] == 1:  # 왼쪽에 길잇음
                while j - 1 >= 0 and arr[i][j - 1] == 1:
                    j -= 1
                i -= 1
            elif j + 1 < 100 and arr[i][j + 1] == 1:  # 오른쪽에 길잇음
                while j + 1 < 100 and arr[i][j + 1] == 1:
                    j += 1
                i -= 1
            else:  # 좌우에 길이 없을때 위로 이동한다.
                i -= 1
        return j

    result = ladder(T)
    # print(result)

    print(f'#{test_case} {result}')


