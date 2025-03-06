# https://school.programmers.co.kr/learn/courses/30/lessons/42840

# 1번수포자: 12345
# 2번수포자: 21232425
# 3번수포자: 3311224455

answers = input()

def solution(arr):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score1 = 0
    score2 = 0
    score3 = 0
    for q in range(len(arr)):
        if q <= len(student1):
            if arr[q] == student1[q]:
                score1 += 1
        else:

        if q <= len(student2):
            if arr[q] == student2[q]:
                score2 += 1
        else:
        if q <= len(student3):
            if arr[q] == student3[q]:
                score3 += 1
        else:



    return