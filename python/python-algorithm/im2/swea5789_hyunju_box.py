import sys
sys.stdin = open("5789.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())  # N: 박스 개수, Q: 작업 개수
    boxes = [0 for _ in range(N)]


    for i in range(Q):
        start, end = map(int, input().split())  # 현재 작업의 시작 박스 번호와 끝 박스 번호 입력
        for j in range(start-1, end):  # 박스 번호는 1번부터 시작하므로 인덱스는 start-1부터 end-1까지
            boxes[j] = i + 1  # 해당 범위 박스에 현재 작업 번호(i+1)를 기록

    print(f'#{tc}', *boxes)