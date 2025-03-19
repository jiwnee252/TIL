# 퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.

def hoare_partition(arr, left, right):
    mid = (left + right) // 2
    pivot = arr[mid]        # pivot을 중앙값으로 선택.
    arr[left], arr[mid] = arr[mid], arr[left]       # pivot을 배열의 왼쪽 끝으로 이동한다.
    i = left + 1    # 왼쪽 포인터 (피벗보다 큰 값 찾기)
    j = right       # 오른쪽 포인터 (피벗보다 작은 값 찾기)

    while i <= j:
        while i <= j and arr[i] <= pivot:   # i가 피벗보다 큰 값이 나올때까지 증가
            i += 1
        while i <= j and arr[j] >= pivot:   # j가 피벗보다 작은 값이 나올때까지 감소
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]  # i와 j를 교환 ( 피벗 기준 작은 값은 왼쪽 큰 값은 오른쪽으로 이동 )

    arr[left], arr[j] = arr[j], arr[left]   # 원래 피벗이 있던 위치 arr[left]와 arr[j]를 교환(피벗을 올바른 위치로 이동)
    return j        # 피벗이 최종적으로 위치한 인덱스를 반환


def quick_sort(arr, left, right):
    if left < right:
        pivot = hoare_partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)             # 피벗 왼쪽부분 정렬
        quick_sort(arr, pivot + 1, right)            # 피벗 오른쪽부분 정렬


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    left = 0
    right = len(arr) - 1

    quick_sort(arr, left, right)

    print(f'#{test_case} {arr[N//2]}')