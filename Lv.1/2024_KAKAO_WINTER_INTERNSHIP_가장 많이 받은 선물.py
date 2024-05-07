#친구들 사이에서 주고받은 선물수 파악해서 다음달에 누가 선물을 많이 받을지 예측
#두 사람 중 더 많은 선물을 준 사람이 다음달에 선물을 하나 받음
#두 사람이 선물을 주고 받지 않았거나, 동일하게 주고 받았으면 선물 지수가 더 큰 사람이 선물을 하나 받음
#(선물지수 : 자신이 친구들에게 준 선물 수 - 받은 선물 수)
#만약 두사람의 선물지수도 같다면 다음 달에 선물을 주고 받지 않는다.

import numpy as np           #zeros 행렬을 위한 numpy 실행

def solution(친구, 선물):
    선물을가장많이받을친구가받을선물의수 = 0
    number = len(친구)
    
    준선물, 받은선물, 다음달받을선물수 = [0 for i in range(number)], [0 for i in range(number)], [0 for i in range(number)]
    선물지수 = []
    선물차이 = np.zeros((number,number))                          #선물 주고받은 상황을 행렬로 나타내기위하여 선언
        
    for j in range(len(선물)) :
        for k in range(number) :
            if 선물[j].split()[0] == 친구[k] : 
                준선물[k] += 1                                    #준 선물 카운트
                for l in range(number) :
                        if 선물[j].split()[1] == 친구[l] :
                            선물차이[k][l] += 1                   #친구[k]가 친구[l]에게 선물 1개 줬음을 표기  
            if 선물[j].split()[1] == 친구[k] : 
                받은선물[k] += 1                                  #받은 선물 카운트
    
    선물지수 = [준선물i - 받은선물i for 준선물i, 받은선물i in zip(준선물, 받은선물)]            #선물지수 = 준선물 - 받은선물
    
    for m in range(number) :
        for n in range(number) :
            if 선물차이[m][n] > 선물차이[n][m] :                   #m과 n을 비교해서 선물을 더 많이 준 친구가 다음달에 선물을 더 많이 받음
                다음달받을선물수[m] += 1            
            elif 선물차이[m][n] == 선물차이[n][m] :
                if 선물지수[m] > 선물지수[n] : 
                    다음달받을선물수[m] += 1
                elif 선물지수[m] < 선물지수[n] :
                    다음달받을선물수[n] += 1
            else :
                다음달받을선물수[n] += 1
    
    선물을가장많이받을친구가받을선물의수 = max(다음달받을선물수) / 2   
    #그중 최대값 선정(단, 주대각선 기준으로 두번씩 중복 계산되기 때문에 나누기2를 실행)
                
    
    return 선물을가장많이받을친구가받을선물의수

#예시 답안 : 2
print(solution(["muzi", "ryan", "frodo", "neo"],["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
