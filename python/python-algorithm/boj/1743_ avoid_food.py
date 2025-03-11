N, M, K = map(int, input().split())
print(N, M, K)   # 통로의 세로 길이, 통로의 가로 길이, 음식물 쓰레기의 개수
arr = [list(map(int, input().split())) for _ in range(K)]   # 음식물이 떨어진 좌표 r, c
print(arr)

# 음식물 중 가장 큰 음식물의 크기를 출력한다.