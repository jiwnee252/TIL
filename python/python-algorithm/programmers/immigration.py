# 최솟값 1 최댓값 max(times) * n

def solution(n, times):
    start = 1                # 최소시간
    end = max(times) * n     # 최대시간
    while start <= end:
        mid = (start + end) // 2        # 중간값
        count = 0           # 심사한 사람의수
        for time in times:   # 각 심사속도 순회하면서
            count += mid // time  # 각 심사관이 mid분동안 심사한 사람의 수의합으로 count업데이트
            if count >= n:      # 심사한사람이 n을넘어가면
                break           # 멈춤
        if count >= n:          # 심사한사람이 n 이상이면.. 시간을줄여주자!
            result = mid
            end = mid - 1       # 시간을 1씩 줄여보고 계속 while 돌리면서 start, end  업데이트.
        elif count < n:
            start = mid + 1     # 심사한사람이 n보다작으면.. 시간이 부족함!
    return result



print(solution(6, [7, 10]))