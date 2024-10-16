def solution(number, n, m):
    cal_n  = number % n == 0
    
    if(not(cal_n)):
        return 0
    
    cal_m = number % m == 0
    if(not(cal_m)):
        return 0
    
    return 1