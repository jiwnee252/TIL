import sys
sys.stdin = open("2001.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N : 배열의크기 M : 파리채크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대 파리의수
    max_f = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            count = 0
            for a in range(i, i + M):
                for b in range(j, j + M):
                    count += arr[a][b]
            # print(count)

            if max_f < count:
                max_f = count


    print(f'#{test_case} {max_f}')