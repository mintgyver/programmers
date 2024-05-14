#고객의 약관 동의를 얻어서 수집된 1~n 번으로 분류되는 개인정보 n개가 있습니다.
#각 약관의 종류마다 개인정보 유효기간이 정해져 있습니다.
#각 개인정보가 어떤 약관으로 수집되어 있는지 주어질때,
#수집된 개인정보가 유효기간이 지났는지 파악하는 solution 함수를 완성하시오.

from datetime import datetime                                           #날짜 계산을 하기 위한 datetime 모듈 사용
from dateutil.relativedelta import relativedelta                        #날짜 계산 시 개월 수 만큼 더하기 위해 relativedelta 사용

def solution(today, terms, privacies):
    
    answer = []
    terms_dic = dict([i.split() for i in terms])                        #약관을 dictionary{약관명, 유효개월수}로 표현
    priva_spl = [i.split(' ') for i in privacies]                       #개인정보를 수집날짜, 약관 종류로 split
    
    today_datetime = datetime.strptime(today, "%Y.%m.%d")               #today를 datetime으로 변경
    
    for i, priva in enumerate(priva_spl, start = 1) : 
        priva_datetime = datetime.strptime(priva[0], "%Y.%m.%d")        #개인정보의 수집날짜를 datetime으로 변경
        a = int(terms_dic[priva[1]])                                    #개인정보 약관 종류에 일치하는 유효개월수 찾기
        nowday = priva_datetime + relativedelta(months = a)             #수집날짜 + 유효개월수 
        if today_datetime >= nowday :                                   
            answer.append(i)                                            #today보다 크면 파기해야 하는 개인정보로 기록
    
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))