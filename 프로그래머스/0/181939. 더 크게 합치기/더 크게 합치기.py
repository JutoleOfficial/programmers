def solution(a, b):
    ab_num = f'{a}{b}'
    ba_num = f'{b}{a}'
    
    return int(ab_num) if int(ab_num) > int(ba_num) else int(ba_num)