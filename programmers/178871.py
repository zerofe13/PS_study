def solution(players, callings):
    answer = []
    
    p_dict = {player:i for i,player in enumerate(players)}
    rp_dict = {i:player for i,player in enumerate(players)}

    for calling in callings:
        index = p_dict[calling]
        temp = rp_dict[index-1]
        
        p_dict[calling] = -1
        p_dict[temp] = index
        p_dict[calling] = index-1
        
        rp_dict[index] = ""
        rp_dict[index-1] = calling
        rp_dict[index] = temp
    
    for i in range(len(players)):
        answer.append(rp_dict[i])
    return answer