# 1. 분할: 리스트의 길이가 1일 때까지 분할
# 2. 정복: 리스트의 길이가 1이 되면 자동으로 정렬됨
# 3. 병합
#   - 왼쪽, 오른쪽 리스트 중
#       작은 원소부터 정답 리스트에 추가하면서 진행
def merge(left, right):
    # 두 리스트를 병합한 결과 리스트
    result = [0] * (len(left) + len(right))
    l = r = 0

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
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


def merge_sort(li):
    if len(li) == 1:
        return li

    # 1. 절반 씩 분할
    mid = len(li) // 2
    left = li[:mid]    # 리스트의 앞쪽 절반
    right = li[mid:]   # 리스트의 뒤쪽 절반

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    # print(left_list, right_list)
    # 분할이 완료되면
    # 2. 병합
    merged_list = merge(left_list, right_list)
    return merged_list


arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)
print(sorted_arr)

'''

def merge_sort(m):
    if len(m) == 1:             # 리스트의 길이가 1이면 재귀 종료.
        return m

    middle = len(m) // 2        # 리스트를 반으로 나누기 위한 인덱스
    left = m[:middle]           # 왼쪽 리스트
    right = m[middle:]          # 오른쪽 리스트

    left = merge_sort(left)     # 왼쪽 재귀호출
    right = merge_sort(right)   # 오른쪽 재귀호출

    return merge(left, right)

인덱스를 이용한 접근:
def merge(left, right):
    result = []
    i, j = 0, 0  # 두 리스트의 인덱스

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])  # 남은 원소 추가
    result.extend(right[j:])

    return result

'''
