def solution(bandage, health, attacks):
    count, i, band_count, current_health = 0, 0, 0, health        #전체 게임 시간, attacks의 차례, 붕대성공횟수, 현재 체력
    
    while count <= attacks[-1][0] :        #공격하는 마지막 시간까지는 count해야 함
        if count == attacks[i][0] :        #공격시간이 되면 공격을 받음
            band_count, band_health = 1, 0  
            attack_health = attacks[i][1]
            i += 1
        elif band_count == bandage[0] :   #붕대 성공 횟수가 차면 추가 회복
            band_count = 1
            band_health = bandage[1] + bandage[2]
            attack_health = 0
        else :                            #그외는 붕대로 체력 회복
            band_count += 1
            band_health = bandage[1]
            attack_health = 0
        count += 1            
        current_health = current_health - attack_health + band_health
        
        if current_health > health :      #초기체력 이상은 회복 불가
            current_health = health
        elif current_health <= 0 :        #체력이 0 이하가 되면 -1 반환
            return -1 
        else :
            answer = current_health

    return answer

print(solution([5,1,5], 30, [[2,10],[9,15],[10,5],[11,5]]))    #test 결과는 5