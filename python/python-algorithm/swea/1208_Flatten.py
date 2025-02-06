import sys
sys.stdin = open("1208_input.txt", "r")

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    N = int(input())  # 덤프횟수
    hlist = list(map(int, input().split()))  # 높이값 목록

    # print(N)
    # print(hlist)
    # print(len(hlist))

    maxh = max(hlist) # 제일 높은 높이값
    minh = min(hlist) # 제일 낮은 높이값

    for i in range(N) : # 덤프를  계속 반복하는데
        maxh_idx = hlist.index(max(hlist))  # 높이가 제일 높은 건물의 인덱스
        minh_idx = hlist.index(min(hlist))  # 높이가 제일 낮은 건물의 인덱스
        if hlist[maxh_idx]- hlist[minh_idx] <= 1 : # 높이차가 0또는1 (평탄화완료) 일경우
            break  # 덤프멈춤
        else :
            # 젤높은상자를 젤낮은상자에덤프 반복
            # 젤큰높이에서 1빼서 젤작은높이에다가 1을더해준다..
            hlist[maxh_idx] -= 1
            hlist[minh_idx] += 1

    result = max(hlist) - min(hlist)

    print(f'#{test_case} {result}')
