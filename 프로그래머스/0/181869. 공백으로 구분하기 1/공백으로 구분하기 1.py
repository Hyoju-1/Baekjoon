def solution(my_string):
    answer = []
    num = 0
    for i in range(0,len(my_string)):
        if my_string[i] == " ":
            answer.append(my_string[num:i])
            num = i+1
    answer.append(my_string[num:])
    return answer