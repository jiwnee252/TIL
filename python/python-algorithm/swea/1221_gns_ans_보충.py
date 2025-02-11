# 샘플 케이스가 내용이 많은 경우에는 Terminal에서 에러가 발생 할 수 있어서..
# file 입출력으로 입력받기
# input() : 표준입력에서 한 줄 읽어오기
import sys

sys.stdin = open('GNS_input.txt', 'r')
# sys.stdout = open('GNS_output.txt','w')
# 정렬에 필수 조건은 서로 크기가 비교가 가능해야 하는데..
# GNS 숫자는 지구 방식으로 비교가 불가 >>> dictionary로 value지정
num_dict = {
    'ZRO': 0,
    'ONE': 1,
    'TWO': 2,
    'THR': 3,
    'FOR': 4,
    'FIV': 5,
    'SIX': 6,
    'SVN': 7,
    'EGT': 8,
    'NIN': 9
}


def bubble_sort(arr):
    for i in range(N - 1):
        # 두 개씩 비교해서 큰거 뒤로 보내기
        for j in range(N - 1):
            # arr[j],arr[j+1] 두 개 비교 해야 합니다.
            # 앞쪽 요소가 더 크면 뒤로 보내기, 크기 비요할 때 dictionary 사용하기
            if num_dict[arr[j]] > num_dict[arr[j + 1]]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    # i번째 최솟값 찾아서 i번 요소와 자리바꾸기
    for i in range(N - 1):
        min_idx = i
        for j in range(i, N):
            if num_dict[arr[min_idx]] > num_dict[arr[j]]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# 1. 요소를 인덱스로 활용할 수 있어야 합니다.
# 2. 최대값과 최소값의 차이가 작아야 효율적입니다.
def counting_sort(arr):
    count = [0] * 10
    # 1. 각 요소 개수 세기
    for i in range(N):
        idx = num_dict[arr[i]]
        count[idx] += 1
    # 2. 누적합구하기 ( 요소가 들어갈 위치 계산)
    for i in range(1, 10):
        # count[i] = count[i] + count[i-1]
        count[i] += count[i - 1]
    # 3. 각 요소 해당 위치에 넣어주기
    sorted_arr = [None] * N
    for i in range(N):
        # arr[i] >>> 얘 위치 찾기
        # 위치는 count가 가지고 있고, count의 인덱스는 dictionary활용
        count[num_dict[arr[i]]] -= 1
        # arr[i]가 들어갈 위치  : count[num_dict[arr[i]]]
        position = count[num_dict[arr[i]]]
        sorted_arr[position] = arr[i]
    return sorted_arr


T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    data = input().split()
    # 내가 입력 잘 받았는지 꼭 확인!!
    # selection_sort(data)
    data = counting_sort(data)
    print(tc)
    print(*data)