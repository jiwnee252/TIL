import sys
sys.stdin = open("1208_input.txt", "r")

# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    N = int(input())  # 덤프횟수
    hlist = list(map(int, input().split()))  # 높이값

    print(N)
    print(hlist)
    
    # 가로길이 100    # 상자의높이 1이상 100이하
    # 덤프횟수 1이상 1000이하

    maxh = max(hlist)
    minh = min(hlist)

    i = 1
    while i <= N :   # 전체 덤프횟수에서.몇회째?
        minh = minh + 1
        maxh = maxh - 1

    print(minh, maxh)


    # 젤높은상자를 젤낮은상자에덤프 반복