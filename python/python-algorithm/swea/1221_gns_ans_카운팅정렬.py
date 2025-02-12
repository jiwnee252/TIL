import sys

sys.stdin = open('input_gns.txt')

# 숫자 체계 정의 (0 ~ 9를 나타내는 단어)
numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
number_to_index = {num: i for i, num in enumerate(numbers)}

T = int(input())
for _ in range(1, T + 1):
    tc, N = input().split()
    N = int(N)
    words = input().split()
    
    # 결과 저장할 배열 초기화
    result = [None] * N

    # 카운팅 배열 초기화 (0 ~ 9까지 각 단어의 등장 횟수)
    count_arr = [0] * 10
    for word in words:
        count_arr[number_to_index[word]] += 1
    
    # 누적합 배열 생성: 각 숫자 단어가 정렬된 결과에서 마지막으로 등장할 인덱스를 계산
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # 안정적인 정렬을 위해 원래 배열을 뒤에서부터 순회하며 결과 배열에 배치
    for i in range(N - 1, -1, -1):
        word = words[i]
        idx = number_to_index[word]
        pos = count_arr[idx] - 1  # 들어갈 위치: 누적 개수 - 1
        result[pos] = word
        count_arr[idx] -= 1  # 해당 단어의 누적 개수 감소

    print(tc)
    print(" ".join(result))
