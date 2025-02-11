import sys
sys.stdin = open("1210.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 2부터 출발한다하면..
    # 현재 기준이되는 2의좌표: arr[i][j]라고 가정한다 , j = 99

    for j in range(100):
        if arr[99][j] == 2:
            i, j = 99, a   # a는 0~99사이
            # for i in range(100):

    while i >= 0:   # i 가 0이 되면 다올라간거니깐...
        while j - 1 >= 0:
            # 만약 왼쪽에만 길이잇으면 -> 왼쪽으로꺾음
            if arr[i][j-1] == 1 and arr[i][j+1] == 0:
                j = a - 1
            # 만약 오른쪽에만 길이잇으면 -> 오른쪽으로꺾음
            elif arr[i][j+1] == 1 and arr[i][j-1] == 0:
                j = a + 1
            # 만약 왼오둘다길이잇으면 -> 그럴일x왜냐면가로지르는경우없으니깐.
            # 만약 왼오둘다길이없고 위로향하는 길만잇으면.
            elif arr[i][j+1] == 0 and arr[i][j-1] == 0:
                i = a - 1   # 위로이동


    print(f'#{test_case} {j}')