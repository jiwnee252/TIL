N = int(input())
Ai = list(map(int, input().split()))
B, C = map(int, input().split())

# 시험장 N개
# i번 시험장의 응시자 Ai명
# 총감독관 B명 감독가능, 시험장당 1명 -> B명
# 부감독관 C명 감독가능, 시험장당 여러명 가능

count = 0
for i in Ai:  # 각 시험장마다 순회하는데
    if B >= i:          # 총감독관이 감독가능한 B명 > i번째 시험장에 있는 학생수
        count += 1          # 총감독관 1명만 필요함.
    else:                   # 총감독관 1명보다 더 필요한경우:
        # (총감독관이 감독하는학생빼고) 남은학생을 C로 나눴을때
        # 일단 나눈만큼 더해주고 + 총감독관 1명분 더해주고
        count += ((i-B) // C) + 1
        if ((i-B) % C) != 0:         # C로안떨어지면 한명더필요한거니까
            count += 1   # 1추가.
print(count)