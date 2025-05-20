import sys
sys.stdin = open("1208.txt", "r")

T = 10
for tc in range(1, T + 1):
    D = int(input())  # 덤프 횟수
    target_arr = list(map(int, input().split()))  # 평탄화 장소

    # 상자의 높이 1이상 100이하
    h_cnt = [0] * 101  # 0번 인덱스 사용안하기 위해 +1을 함

    # 최대와 최소를 저장하기 위한 변수
    min_value = target_arr[0]
    max_value = target_arr[0]

    # 모든 높이의 개수를 세자
    for target in target_arr:
        h_cnt[target] += 1  # 해당 높이의 개수

        if min_value > target:
            min_value = target
        if max_value < target:
            max_value = target

    for _ in range(D):  # 덤프 횟수 만큼 반복
        # 덤프 횟수는 남았지만 더이상 평탄화 할 필요 없는 경우
        if max_value - min_value <= 1:
            break
        # 최대 높이의 값을 최소 높이로
        # 결국 최대 높이의 갯수 1개 감소
        #  최대 높이에서 1개 줄었기 때문에
        #  최대 개수 1감소, -1 요소에 값 증가
        # 최소 높이의 갯수 1개 증가
        #  최소 높이에서 1개 늘었기 때문에
        #  최소 개수 1감소, +1 요소에 값 증가

        h_cnt[max_value] -= 1
        h_cnt[max_value - 1] += 1

        h_cnt[min_value] -= 1
        h_cnt[min_value + 1] += 1

        # 최대 혹은 최소에 더 이상 옮길 상자가 없는 경우
        if h_cnt[max_value] == 0:
            max_value -= 1
        if h_cnt[min_value] == 0:
            min_value += 1

    result = max_value - min_value
    print(f'#{tc} {result}')