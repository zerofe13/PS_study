import sys
sys.setrecursionlimit(10000)
def solution(word):
    answer = 0
    word = list(word)
    word_order=['A','E','I','O','U']
    def search(com_word,depth):
        nonlocal answer
        if com_word == word:
            answer = depth
            return
        if len(com_word) >= 5:
            while com_word[-1] == 'U':
                com_word = com_word[:-1]
            temp = word_order.index(com_word[-1])
            com_word[-1] = word_order[(temp+1)%5]
        else:
            com_word.append("A")
        search(com_word,depth+1)
    search([],0)
    return answer

# dictionary = []
# def recursion(p, step):
#     if step == 6:
#         return
#     if p != '':
#         dictionary.append(p)
#     for c in ['A', 'E', 'I', 'O', 'U']:
#         recursion(p+c, step+1)
 
# def solution(word):
#     answer = 0
#     recursion('', 0)
#     for i in range(len(dictionary)):
#         if dictionary[i] == word:
#             answer = i+1
#             break
#     return answer

print(solution("U"))
