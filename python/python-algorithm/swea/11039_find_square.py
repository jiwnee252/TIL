import sys
sys.stdin = open("11039_sample_in.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    di = []
    dj = []
    
    # print(f'{test_case} {result}'})
    max_result = 0
    # 순회하다가
    for i in range(N):
        for j in range(N):
            # 1을 발견하면
            if arr[i][j] == 1:
                # 오른쪽이 0이 될때까지 계속 탐색한다
                    i += 1
                    j += 1
                    while arr[i][j] == 0:

                
                # 오른쪽이 0이되면 멈춘다 -> 멈춘좌표로 i, j를 갱신한다음, 거기부터 다시 시작
                # 오른쪽에 있는 1을 전부 탐색했으면
                # 해당 1의 아래쪽을 전부 탐색.
                # 아래쪽이 0이되면 멈춘다
                # 그러면 오른쪽, 아래쪽에 있는 1을 모두 탐색 했으므로
                # 우하 꼭짓점 좌표 - 좌상 꼭짓점 좌표 해서 값을 찾아서
                # 방금 찾은 값이 max_result 보다 크면 max_result를 갱신한다.



                #  만약 오른쪽 탐색했는데 1이 없고
                # 아래쪽도 탐색했는데도 1이 없으면
                # 프린트 1
        
