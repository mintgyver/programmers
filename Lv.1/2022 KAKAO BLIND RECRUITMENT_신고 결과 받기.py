#각 유저는 한번에 한 명의 유저를 신고할 수 있습니다.
#한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
#k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.


def solution(id_list, report, k):
    
    id_len = len(id_list)
    warn = [0 for i in range(id_len)]                   #경고 횟수 파악을 위한 리스트
    id_list_warn = []                                   #경고 받은 아이디 리스트
    answer = [0 for i in range(id_len)] 
    
    report_set = list(set(report))                      #리포트 중복 제거를 위한 set
    report_name = [i.split() for i in report_set]       #split을 통해 신고자와 신고대상자 분리
    
    for i in report_name : 
        warn[id_list.index(i[1])] += 1                  #신고대상자 카운트
                        
    for i in range(id_len) : 
        if warn[i] >= k :                               #k번 이상이면 이름 기록
            id_list_warn.append(id_list[i])
        
    for i in report_name : 
        if i[1] in id_list_warn :                       #기록된 이름 신고자 카운트 하기
            answer[id_list.index(i[0])] += 1
                            
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
