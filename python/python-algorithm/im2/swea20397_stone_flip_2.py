import sys
sys.stdin = open("20397.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 돌의 갯수, M: 뒤집기 횟수
    stone_list = list(map(int, input().split()))
    # print(N, M, stone_list)
    # M번의 i, j
    for cnt in range(M):
        i, j = map(int, input().split())  # i: 기준점 (번째, index 아님), j: 마주보는 돌의 갯수
        # print(i, j)
        idx = i - 1  # 기준 인덱스
        for di in range(1, j + 1):  # 1부터 j까지 비교해야 하기 때문에 j+1
            # 마주 보는 돌의 인덱스
            left_idx = idx - di  # 왼쪽 돌 인덱스
            right_idx = idx + di  # 오른쪽 돌 인덱스

            # 인덱스 값에 변화가 있다면!
            # 해당 인덱스가 리스트 범위 내인지 반드시 확인을 해야 함!!
            # 범위를 벗어나면 뒤집기 중지!
            if left_idx < 0 or right_idx >= N:
                break

            # 두 돌의 색상이 다르다면 다음 돌을 비교
            if stone_list[left_idx] != stone_list[right_idx]:
                continue  # 다음 돌 비교

            # 색상이 같다면 색상을 변경 (두 돌의 색상이 같기 때문에 하나만 확인하면 됨)
            if stone_list[left_idx] == 1:
                stone_list[left_idx] = 0
                stone_list[right_idx] = 0
            else:
                stone_list[left_idx] = 1
                stone_list[right_idx] = 1

    print(f'#{tc}', *stone_list)
