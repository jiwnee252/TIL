import sys

sys.stdin = open('4831.txt')

T = int(input())
for tc in range(1, T + 1):
    # K: 최대 갈 수 있는 거리 / M: 충전기 정류장 갯수 / N: 종점
    K, N, M = map(int, input().split())
    station = set(map(int, input().split()))  # list로 해도 되지만 set 이 바로 접근 할 수 있어 빠르다.
    charge = 0

    # 충전되서 가장 멀리 간 후 한 칸씩 뒤로 오면서 충전소 체크
    # 한 칸씩 뒤로 오다가 최근 출발한 위치에 돌아 온다면 이동 불가
    # 버스의 이동 거리
    move = K  # 최대 충전 거리만큼 이동
    # 최근 위치 저장
    last = 0
    while move < N:  # 종점에 도착하기 전 까지 반복
        for _ in range(K):  # K 만큼 한 칸씩 뒤로 되돌아가기
            if move in station:  # 이동한 거리에 충전소가 있는지 확인
                charge += 1  # 충전 횟수 증가
                break
            move -= 1  # 한 칸씩 뒤로 이동
        # 원래 위치로 돌아 왔는지 확인
        if last == move:
            charge = 0
            break

        last = move  # 이동 위치 저장
        move += K  # 최대 이동

    print(f'#{tc} {charge}')
