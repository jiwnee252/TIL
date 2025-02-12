import sys
sys.stdin = open("23148_4831_electric_bus.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

    KNM = (input().split())   # 노선수
    K = int(KNM[0])  # 한번 충전으로 최대한 이동할 수 잇는 정류장 수
    N = int(KNM[1])  # N번 정류장이 종점 ( 총 정류장의 개수 = N+1 )
    M = int(KNM[2])  # 충전기가 설치된 정류장의 개수
    stations = list(map(int, (input().split())))  # 충전기가 설치된 정류장의 번호 리스트

    # 종점에 도착하기 위한 최소 충전횟수?
    charge_count = 0  # 충전횟수
    charge_station = 0  # 마지막으로 충전한 정류장의 번호

    for station in range(N+1): # 총정류장의개수를순회하면서
        # charge_station에 K를 더해가면서업데이트. (직전에 충전한 정류장의번호)
        # 업데이트횟수는 M이하임
        charge_station += K
        # 만약에 charge_station이 N을 초과하면 break
        if charge_station >= N:
            break
            # 만약 초과하지않을경우
            # 


    # print(KNM)
    print(K)
    print(N)
    print(M)
    print(stations)

    # print(f'#{}')