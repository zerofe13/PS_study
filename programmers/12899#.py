#124 나라의 숫자
def solution(n):
    answer = ''
    rev_base = ''
    while n>0:
        n,mod= divmod(n,3)
        if mod == 0:
            rev_base += str('4')
            n = n-1
        elif mod == 1:
            rev_base += str('1')
        else:
            rev_base += str('2')
    answer = rev_base[::-1]
    return answer