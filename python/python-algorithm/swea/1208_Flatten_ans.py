import sys

sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    dump = int(input())  # 상자를 옮길 수 있는 횟수
    box_heights = list(map(int, input().split()))

    # 여기 왜 언더바로 하나요 ? =>
    # 이 for문은 반복문에 불가하다.
    for _ in range(dump):

        max_idx, max_box_height = 0, box_heights[0]
        min_idx, min_box_height = 0, box_heights[0]

        for i in range(len(box_heights)):
            # 최대값 찾기
            if box_heights[i] > max_box_height:
                max_idx, max_box_height = i, box_heights[i]
            # 최소값 찾기
            if box_heights[i] < min_box_height:
                min_idx, min_box_height = i, box_heights[i]

        # 평탄화 높이 차이가 1이하이면, 굳이 평탄화를 할 필요가 없다.
        if max_box_height - min_box_height <= 1:
            break

        box_heights[max_idx] -= 1
        box_heights[min_idx] += 1

    # 평탄화 끝나고 나서도, 또 최대 높이의 상자와 최소 높이의 상자가 바뀌었을 수도 있다.
    print(f'#{test_case} {max(box_heights) - min(box_heights)}')
