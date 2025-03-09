# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(arr):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []
    for i in range(len(arr)):
        if arr[i] == student1[i % len(student1)]:
            score[0] += 1
        if arr[i] == student2[i % len(student2)]:
            score[1] += 1
        if arr[i] == student3[i % len(student3)]:
            score[2] += 1


    return result
    
    # 가장 높은 점수를 받은 사람이 여럿일 경우 return 하는 값을 오름차순 정렬한다

answers = input()
print(solution(answers))