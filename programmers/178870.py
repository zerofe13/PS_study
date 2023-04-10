def solution(sequence, k):
    answer = []
    start, end = 0,0
    
    num_sum = sequence[0]
    while start<=end and end < len(sequence):
        
        if num_sum ==k:
            answer.append((end-start,start,end))
        
        if num_sum <k or end == start:
            end+=1
            if end < len(sequence):
                num_sum += sequence[end]
            continue
            
        num_sum -= sequence[start]
        start += 1
        
    answer.sort(key=lambda x:x[0])
    return [answer[0][1],answer[0][2]