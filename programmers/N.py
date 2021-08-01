def solution(N, number):
    dp = [set() for _ in range(9)]
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        for j in range(1,i):
          for number1 in dp[j]:
              for number2 in dp[i-j]:
                  dp[i].add(number1 + number2)
                  dp[i].add(number1 - number2)
                  dp[i].add(number1 * number2)
                  if number2 != 0:
                      dp[i].add(number1 // number2)
        if number in dp[i]:
            return i
    return -1

print(solution(5,12))