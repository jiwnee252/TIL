def merge(left, right):
    global count
    # 두 리스트를 병합한 결과 리스트
    result = [0] * (len(left) + len(right))
    l = r = 0

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
    if left[-1] > right[-1]:
        count += 1

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    # 오른쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


def merge_sort(lst):
    if len(lst) == 1:
        return lst

    # 1. 절반 씩 분할

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    # print(left_list, right_list)
    # 분할이 완료되면
    # 2. 병합
    merged_list = merge(left_list, right_list)
    return merged_list


# arr = [69, 10, 30, 2, 16, 8, 31, 22]
# sorted_arr = merge_sort(arr)
# print(sorted_arr)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    count = 0   # 오른쪽 원소가 먼저 복사되는 경우

    arr_ = merge_sort(arr)
    result = arr_[N//2]

    print(f'#{tc} {result} {count}')