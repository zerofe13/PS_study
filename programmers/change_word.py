from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    def match(begin,word):
        count = 0
        for i in range(len(begin)):
            if begin[i] != word[i]:
                count += 1
        if count == 1:
            return True
        else:
            return False
    words.append(begin)
    check=[0] * len(words)
    queue = deque()
    queue.append(begin)
    check[-1] = 0
    while queue:
        compare = queue.popleft()
        if compare == target:
            answer = check[words.index(target)]
            break
        for word in words:
            if match(compare,word) and check[words.index(word)]==0:
                queue.append(word)
                check[words.index(word)] = check[words.index(compare)]+1

    return answer

begin = "hit"
target = "cog"
words = ["hot","dot","dog","lot","log","cog"]
print(solution(begin,target,words))