def solution(my_string, is_suffix):
    num = len(my_string)-len(is_suffix)

    return 1 if my_string[num:] == is_suffix else 0