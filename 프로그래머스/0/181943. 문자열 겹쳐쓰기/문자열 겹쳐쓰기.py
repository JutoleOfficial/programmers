def solution(my_string, overwrite_string, s):
    answer = my_string[:s]
    answer += overwrite_string
    answer += my_string[len(answer):]
    return answer