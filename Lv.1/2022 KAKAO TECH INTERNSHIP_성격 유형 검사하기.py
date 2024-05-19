#나만의 성격 유형 검사지를 만들려고 합니다.
#성격 유형 검사는 다음과 같은 4개의 지표로 성격을 구분합니다.
#1번지표 : 라이언형(R), 튜브형(T)
#2번지표 : 콘형(C), 프로도형(F)
#3번지표 : 제이지형(J), 무지형(M)
#4번지표 : 어피치형(A), 네오형(N)

#검사지에는 총 n개의 질문이 있고 각 질문은 7개의 선택지가 있습니다.
#매우 비동의, 비동의, 약간 비동의, 모르겠음, 약간 동의, 동의, 매우 동의

#각 질문은 1가지 지표로 성격 유형 점수를 판단합니다.
#매우 비동의 : 네오형 3점, 비동의 : 네오형 2점, 동의 : 네오형 1점
#모르겠음 : 어떤 성격 유형도 점수를 얻지 않습니다.
#약간 동의 : 어피치형 1점, 동의 : 어피치형 2점, 매우 동의 : 어피치형 3점

#각 지표에서 높은 점수를 받은 성격 유형이 검사자의 성격입니다.
#단 성격 유형 점수가 같으면, 사전순으로 빠른 성격 유형을 검사자의 유형이라고 판단합니다.
#이떄 성격 유형을 return하는 solution을 완성하시오.

from collections import defaultdict                         #dictionary 초기화를 위해 사용

def solution(survey, choices):
        
    case = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']         #성격유형을 key값으로 설정
    survey_dic = dict.fromkeys(case)
    survey_dic = defaultdict(int)                           #value값은 정수로 설정
    answer = ''
        
    for i, survey in enumerate(survey) :   
        if choices[i] <= 4 :                                #점수가 4보다 낮으면 해당 검사의 첫번째 유형의 점수로 저장
            survey_dic[survey[0]] += (4 - choices[i])
        else :                                              #점수가 4보다 크면 해당 검사의 두번째 유형의 점수로 저장
            survey_dic[survey[1]] += (choices[i] - 4)
            
    answer = answer + 'R' if survey_dic['R'] >= survey_dic['T'] else answer + 'T'       #비교하여 높은점수로 성격유형 판단
    answer = answer + 'C' if survey_dic['C'] >= survey_dic['F'] else answer + 'F'
    answer = answer + 'J' if survey_dic['J'] >= survey_dic['M'] else answer + 'M'
    answer = answer + 'A' if survey_dic['A'] >= survey_dic['N'] else answer + 'N'    
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
# 정답은 "TCMA"