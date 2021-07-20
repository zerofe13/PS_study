
def solution(tickets):
    answer = []
    check = [0] * len(tickets) # 방문 체크 배열
    air_path = [0] * len(tickets) # 공항 경로 배열
    mem_path = [] # 최종 경로 저장 배열

    tickets.sort()
    def DFS(ticket,depth,path):
        nonlocal mem_path
        for i in range(len(tickets)):
            if ticket[1] == tickets[i][0] and check[i] == 0:
                check[i] = 1 # 방문
                air_path[path] = i #경로 저장
                DFS(tickets[i],depth+1,i)
                check[i] = 0 # 재귀 탈출 후 방문 다시 0
        if depth == len(tickets)-1 and not mem_path: # 저장경로가 첫번째 경우가 알파벳 우선순위 
            air_path[path] = -1
            mem_path = air_path[:] #copy
            return
        if mem_path: #백트랙킹
            return

    for i in range(len(tickets)):
        check[i] = 1
        DFS(tickets[i],0,i)
        if mem_path and tickets[i][0] == "ICN": #시작 공항 인천
            # 경로를 이용하여 answer 에 공항 str 저장 
            answer.append(tickets[i][0])
            answer.append(tickets[i][1])
            path_i = i
            while True:
                if mem_path[path_i] == -1:
                    break
                n_i = mem_path[path_i]
                answer.append(tickets[n_i][1])
                path_i = n_i
            break
        #초기화
        check = [0] * len(tickets) 
        air_path = [0] * len(tickets)
        mem_path = []
    return answer

ticket = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]


print(solution(ticket))