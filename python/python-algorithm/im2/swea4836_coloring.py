import sys
sys.stdin = open("4836.txt", "r")

T = int(input())  # 테스트 케이스 개수 입력받기

for tc in range(1, T + 1):  # 테스트 케이스 개수만큼 반복
    N = int(input())  # 색칠할 영역의 개수 입력받기
    arr = [[0]*10 for _ in range(10)]  # 10x10 크기의 격자 배열 생성 (초기값 0)
    ans = 0  # 보라색(겹쳐진 부분) 개수를 저장할 변수 초기화

    for n in range(N):  # 주어진 색칠할 영역 개수만큼 반복
        r1, c1, r2, c2, color = map(int, input().split())  # 색칠할 영역 좌표와 색상 입력받기

        # 지정된 영역을 색칠
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color  # 현재 칸에 색상 값 더하기 (1: 빨강, 2: 파랑)

    # 보라색 영역(빨강 + 파랑 = 3) 개수 카운트
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:  # 값이 3이면 (빨강+파랑이 겹친 경우)
                ans += 1  # 보라색 영역 개수 증가

    print(f'#{tc} {ans}')  # 결과 출력