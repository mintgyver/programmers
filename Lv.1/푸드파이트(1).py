#푸드 파이트 대회
#이 대회에서 선수들은 1대 1로 대결하며, 대결마다 음식의 종류와 양이 바뀝니다.
#한 선수는 제일 왼쪽부터, 다른선수는 오른쪽부터 순서대로 먹으며
#중앙에 물을 배치합니다.
#대회의 공정성을 위해 두 선수가 먹는 음식의 종류와 양이 같아야 하며, 음식을 먹는 순서도 같아야 합니다.
#대회에서는 칼로리가 낮은 음식을 먼저 먹을 수 있게 배치합니다.
#음식의 양을 칼로리가 적은 순서대로 나타내는 정수배열 food가 있을때, 대회 음식 배치를 나타내는 문자열을 return합니다.
#food[0]은 항상 1입니다.

#예를 들어 칼로리가 적은 순서대로 1번 음식 2개, 2번 음식 3개 있을 경우,
#물을 편의상 0번 음식이라고 하면
#음식 배치는 12021 입니다(2번 음식 1개는 대회에 사용되지 못합니다.)

def solution(food):
    
    food_len = len(food)
    food_num, result_food = [], []
    food_cal = 0
    
    for i in range(food_len) :
        food_num.append(food[i] // 2)
    
    for i in range(food_len) : 
        for j in range(food_num[i]) : 
            result_food.append(food_cal)
        food_cal += 1
    
    answer = result_food + [0] + list(reversed(result_food))
            
    return ''.join(map(str, answer))

print(solution([1,3,4,6]))
