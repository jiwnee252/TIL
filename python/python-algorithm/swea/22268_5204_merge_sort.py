def merge_sort(m):
    if len(m) == 1:             # 리스트의 길이가 1이면 재귀 종료.
        return m

    middle = len(m) // 2        # 리스트를 반으로 나누기 위한 인덱스
    left = m[:middle]           # 왼쪽 리스트
    right = m[middle:]          # 오른쪽 리스트

    left = merge_sort(left)     # 왼쪽 재귀호출
    right = merge_sort(right)   # 오른쪽 재귀호출

    return merge(left, right)


def merge(left, right):
    result = []   # 병합된 정렬 결과를 저장할 리스트

    count = 0
    if left[-1] > right[-1]:
        count += 1

    while len(left) > 0 or len(right) > 0:  # 둘 중 하나라도 남아있으면 반복
        if len(left) > 0 and len(right) > 0:  # 둘 다 값이 있으면 비교
            count = 0
            if left[-1] > right[-1]:
                count += 1


            if left[0] <= right[0]:  # 왼쪽 값이 작으면 왼쪽 값을 추가
                result.append(left.pop(0))
            else:  # 오른쪽 값이 작으면 오른쪽 값을 추가
                result.append(right.pop(0))

        elif len(left) > 0:  # 왼쪽 리스트에 값이 남아 있으면 추가
            result.append(left.pop(0))

        elif len(right) > 0:  # 오른쪽 리스트에 값이 남아 있으면 추가
            result.append(right.pop(0))

    return count  # 정렬된 리스트 반환


'''

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
T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{test_case} {merge_sort(arr)}')

'''

2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

'''