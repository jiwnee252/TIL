import sys
sys.stdin = open("22375.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    # Ai의 첫 번째 칸과 Bi의 첫 번째 칸을 비교
    #  다르면 해당 위치의 스위치를 변경 해야 함
    #    스위치를 변경하게 되면 해당 위치 부터 N까지의 켜짐 => 꺼짐 / 꺼짐 => 켜짐 변환
    #  중요한 것은 변경하는 횟수
    #  같으면 스위치 변경할 필요 없음
    count = 0
    for idx in range(N):
        if Ai[idx] != Bi[idx]:
            count += 1  # 스위치 횟수 증가
            for jdx in range(idx, N):
                # 켜짐/꺼짐 스위칭
                if Ai[jdx] == 1:
                    Ai[jdx] = 0
                else:
                    Ai[jdx] = 1

    print(f'#{tc} {count}')