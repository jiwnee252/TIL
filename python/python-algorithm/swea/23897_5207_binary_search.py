T = int(input())

# 양쪽구간 번갈아 선택을 만족하는 숫자를 구하기.
def bin_search(lst, target):
    start = 0
    end = len(lst) - 1
    search = None    # 어떤 구간을 탐색했는지 저장해줄것.
    while start <= end:
        m = (start + end) // 2
        if lst[m] == target:
            return True
        else:
            # 오른쪽구간 탐색은 'r' 왼쪽구간 탐색은 'l'로 표시 해줄것임
            if lst[m] < target:
                if search == 'r': # 이미 오른쪽구간 탐색을 했었다면 그냥끝냄
                    break
                else:
                    start = m + 1
                    search = 'r'   # 오른쪽 구간 탐색함을 표시
            elif lst[m] > target:
                if search == 'l': # 이미 왼쪽구간 탐색을 했었다면 그냥끝냄
                    break
                else:
                    end = m - 1
                    search = 'l'   # 왼쪽 구간 탐색함을 표시
        # return True
    return False

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    count = 0
    for num in B:
        if num in A and bin_search(A, num) == True:
                count += 1

    print(f'#{test_case} {count}')

