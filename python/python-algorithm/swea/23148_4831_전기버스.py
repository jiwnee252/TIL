import sys
sys.stdin = open("23148_4831_전기버스.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    KNM = (input().split())
    K = int(KNM[0]) # 한번 충전으로 최대한 이동할 수 잇는 정류장 수
    N = int(KNM[1]) # N번 정류장이 종점 ( 총 정류장의 개수 = N+1 )
    M = int(KNM[2]) # 충전기가 설치된 정류장의 개수
    Mlist = list(map(int, (input().split()))) # 충전기가 설치된 정류장의 번호 리스트
    # 충전을 최소 몇번 해야 종점에 도착할 수 잇나요?
    # 출발지 ( Mlist[0] 에는 반드시 충전기가 있음.)
    
    # 한번에 K개의 정류장만 이동할수 잇으니깐 반드시 Mlist[i+1] - Mlist[i] <= K

    charge_count = 0  # 충전한횟수
    current = 0  # 현재 내가 있는 정류장 번호
    last_charge = 0  # 마지막으로 충전한 정류장 번호

    for i in range(M-1) : # 0번부터 m-2
        if Mlist[i+1] - Mlist[i] > K : # 충전 못하는경우
            charge_count = 0
            break
        else: # 충전가능한경우
            for j in range(1, len(Mlist)) :
                if Mlist[j] - last_charge >= K :
                    last_charge = Mlist[j-1]
                    charge_count += 1
    print(charge_count)
    print(f'#{test_case} {charge_count}')