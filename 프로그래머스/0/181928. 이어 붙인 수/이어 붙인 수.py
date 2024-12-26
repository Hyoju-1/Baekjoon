def solution(num_list):
    answer = 0
    even =''
    odd = ''
    for i in num_list:
        if int(i) % 2 == 0:
            even= even + str(i) 
        else:
            odd = odd + str(i)
    answer = int(odd)+int(even)
            
    return answer