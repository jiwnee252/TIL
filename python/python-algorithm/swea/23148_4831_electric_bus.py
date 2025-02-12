import sys
sys.stdin = open("23148_4831_electric_bus.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    KNM = (input().split())   # 노선수
    K = int(KNM[0])  # 한번 충전으로 최대한 이동할 수 잇는 정류장 수
    N = int(KNM[1])  # N번 정류장이 종점
    M = int(KNM[2])  # 충전기가 설치된 정류장의 개수
    charge_stations = list(map(int, (input().split())))  # 충전기가 설치된 정류장의 번호 리스트
    charge_stations.insert(0, 0)  # 0번정류장엔 무조건 충전기 잇으니깐 0번인덱스에 0을추가 # 헷갈리니깐 ㅜㅜ

    charge_count = 0  # 충전횟수
    # last_station = 0 # 마지막으로 충전한 정류소
    current_station = 0 # 현재 있는 정류소

    for _ in range(N):
        # 한번갈때 최대 K만큼 갈수잇으니깐
        # K만큼가보고..못가면 K-1만큼가보구..못가면K-2..
        for k in range(K, 0, -1):
            if current_station + k in charge_stations:
                charge_count += 1
                current_station += k
                break
        else:
            charge_count = 0
            break
        if current_station + K >= N:  # 이동햇는데 종점되면? 끝
            break

    print(f'#{test_case} {charge_count}')








    '''
    for i in range(1, len(charge_stations)):
        # stations의 i-1번째 정류장과 i번째 정류장 사이의 거리가 K보다 크면 충전기 설치 잘못된거임.
        # 출발지에는 항상 충전기가 설치되어있지만 충전횟수에는 포함하지않음에유의한다..
        if charge_stations[i] - charge_stations[i - 1] > K:
            charge_count = 0
            break
        else:  # 만약 충전기설치에 문제가 없다면??
            last_station = 0  # 마지막으로 충전한 정류장의 번호를 0이라고 가정
            if charge_stations[i] - last_station > K: # 만약 i번째충전소와 마지막으로충전한정류장 간의 거리가 K보다 커진다면 마지막충전한정류장은 i-1번째 충전소 ㅁ 뭔소리지
                last_station = charge_stations[i-1]
                charge_count += 1

                # 근데 i가0이면
    print(f'#{test_case} {charge_count}')
    '''