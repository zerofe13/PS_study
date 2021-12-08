# 2021 dev-matching 로또의 최고 순위와 최저 순위
def rank (num):
    if num == 6: return 1
    elif num == 5: return 2
    elif num == 4: return 3
    elif num == 3: return 4
    elif num == 2: return 5
    else: return 6

def solution(lottos, win_nums):
    answer = []
    count = 0
    zero_count = 0
    for lotto in lottos:
        if lotto in win_nums:
            count += 1
        elif lotto == 0:
            zero_count += 1
    answer = [rank(count+zero_count),rank(count)]
    return answer