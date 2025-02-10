import sys
sys.stdin = open("4843_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))

    def selection_sort(num, N):
        for i in range(N-1):
            min_idx = i
            for j in range(i+1, N):
                if num[min_idx] > num[j]:
                    min_idx = j
            num[i], num[min_idx] = num[min_idx], num[i]
        return num

    sorted_num = selection_sort(num, N)

    special_sorted_num = []

    while len(num) > 0:
        special_sorted_num.append(sorted_num[-1])
        sorted_num.pop()
        special_sorted_num.append(sorted_num[0])
        sorted_num.pop(0)

    # 10개까지만 출력
    # result = special_sorted_num[:10]

    result = ' '.join(map(str, special_sorted_num[:10]))

    print(f'#{test_case} {result}')
