import sys
sys.stdin = open("22339.txt", "r")


T = int(input())
for tc in range(1, T+1):
    num = int(input())
    arr = list(map(int, input().split()))
    count = [0] * 31  # 크기별 당근 개수를 저장할 리스트 (크기 범위: 1~30)
    carrot = [0]  # 누적 합을 저장할 리스트, 초기값은 0

    # 각 크기의 당근 개수를 카운트
    for i in arr:
        count[i] += 1  # 해당 크기의 인덱스에 1씩 증가

    # 존재하는 당근 크기만 누적합 리스트에 추가
    for i in range(1, 31):  # 1부터 30까지 확인
        if count[i]:  # 해당 크기의 당근이 존재한다면
            carrot.append(count[i] + carrot[-1])  # 누적합 계산 후 carrot 리스트에 추가

    # 당근을 3묶음으로 나눌 수 없을 경우 (묶음이 3개 이상이 아니면 -1 출력)
    if len(carrot) <= 3:  # 최소한 3개의 그룹을 만들 수 있어야 함
        print(f'#{tc} {-1}')
    else:
        result = 99999999  # 최소값을 찾기 위한 초기 값 설정

        # 당근 묶음을 3개로 나누는 모든 가능한 경우 탐색
        for i in range(1, len(carrot) - 2):  # 첫 번째 구간 끝 인덱스
            for j in range(i + 1, len(carrot) - 1):  # 두 번째 구간 끝 인덱스
                # 각각의 그룹 개수 계산
                small = carrot[i]                       # 첫 번째 그룹: 0 ~ i
                middle = carrot[j] - carrot[i]          # 두 번째 그룹: i+1 ~ j
                big = carrot[-1] - carrot[j]            # 세 번째 그룹: j+1 ~ 마지막

                # 가장 큰 그룹과 가장 작은 그룹 간의 차이를 계산
                temp = max(small, middle, big) - min(small, middle, big)
                # 현재 결과보다 더 작은 차이가 있다면 갱신
                result = min(result, temp)


        print(f'#{tc} {result}')