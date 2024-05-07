def solution(id_list, report, k):
    
    id_len = len(id_list)
    warn = [0 for i in range(id_len)]
    id_list_warn = []
    answer = [0 for i in range(id_len)]
    
    report_set = list(set(report))
    report_name = [i.split() for i in report_set]
    
    for i in report_name : 
        warn[id_list.index(i[1])] += 1
                        
    for i in range(id_len) : 
        if warn[i] >= k :
            id_list_warn.append(id_list[i])
        
    for i in report_name : 
        if i[1] in id_list_warn :
            answer[id_list.index(i[0])] += 1
                            
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
