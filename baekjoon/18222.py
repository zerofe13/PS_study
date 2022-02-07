k = int(input())
def solution(n):
    if n == 0:
        return 0
    if n%2 == 0 :
        return solution(n//2)
    if n%2 == 1:
        return 1-solution(n//2)
print(solution(k-1))