import sys
sys.stdin = open("6485.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    """
    핵심은 버스 노선의 번호는 최대 5000 -> 모든 버스 정류장을 미리 초기화 / 그렇지 않은 경우 시간 초과
    """
    all_stations = [0 for _ in range(1, 5001)] # 버스 정류장 초기화
    N = int(input())     # 버스 노선의 개수

    for _ in range(N): # 버스 노선의 개수 만큼 반복을 돌면서
        A, B = map(int, input().split())     # A이상 B이하의 정류장을 변수에 담고
        # 버스 노선 시작 ~ 끝까지 체크
        # index 기준으로는 -1을 해줘야 첫 번째 노선에 체크 된다.
        for i in range(A - 1, B):
            # 해당 노선에 포함되는 정류장은 1로 체크
            all_stations[i] += 1

    # 체크 해야 할 정류장 번호의 개수
    P = int(input())

    bus_stops = [] # 버스 정류장
    for _ in range(1, P + 1):
        check = int(input()) # check 할 정류장 번호

        # 해당하는 인덱스(정류장)에 버스 노선의 개수를 찾아서 bus_stops에 넣기
        # index라서 -1이 필요
        bus_stops.append(all_stations[check - 1])

    result = ' '.join(map(str, bus_stops))
    print(f'#{tc} {result}')

'''
for tc in range(1, T + 1):
    # 버스 정류장은 1번부터 5000번까지 존재
    # 각 인덱스는 해당 정류장을 지나가는 버스 노선의 개수를 저장할 공간
    stations = [0] * 5000

    N = int(input())  # 버스 노선의 개수

    for _ in range(N):
        A, B = map(int, input().split())  # 각 버스 노선의 시작 정류장 A, 끝 정류장 B 입력받기

        # A부터 B까지 모든 정류장에 대해 버스가 지나간다는 의미니까
        # stations 리스트의 A-1부터 B-1까지 인덱스를 1씩 증가시킴
        for i in range(A - 1, B):
            stations[i] += 1

    P = int(input())  # 우리가 확인하고 싶은 정류장의 개수

    # 확인하고 싶은 정류장 번호들을 하나씩 입력받아서
    # stations[번호 - 1]에 들어있는 값을 리스트에 저장
    # → 그 정류장을 지나가는 버스 노선의 수
    result = [str(stations[int(input()) - 1]) for _ in range(P)]

    # 결과 출력: 테스트 케이스 번호와 함께 공백으로 구분된 문자열 출력
    print(f'#{tc} {" ".join(result)}')
'''