
def solution(tickets):
    answer = []
    check = [0] * len(tickets)
    air_path = [0] * len(tickets)
    mem_path = [0] * len(tickets)

    tickets.sort()
    def DFS(ticket,depth,path):
        nonlocal mem_path
        
        for i in range(len(tickets)):
            if ticket[1] == tickets[i][0] and check[i] == 0:
                check[i] = 1
                air_path[path] = i
                DFS(tickets[i],depth+1,i)
        if depth == len(tickets)-1:
            mem_path = air_path
            return

    for i in range(len(tickets)):
        check[i] = 1
        DFS(tickets[i],0,i)
        if mem_path != [0]*len(tickets):
            answer.append(tickets[i][0])
            answer.append(tickets[i][1])
            for _ in range(tickets)-1:
                
    return answer

ticket = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]


print(solution(ticket))