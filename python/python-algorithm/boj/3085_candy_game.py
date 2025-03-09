for test_case in range(1, T+1):
    # C 빨간색 P 파란색 Z 초록색 Y 노란색
    # 사탕의 색이 다른 인접한 두 칸을 골라서
    # 사탕을 교환
    N = int(input())
    arr = [[0] * N for _ in range(N)]