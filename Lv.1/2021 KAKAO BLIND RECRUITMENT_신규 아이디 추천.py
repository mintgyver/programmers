#새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때,
#입력한 아이디와 유사하면서 규칙에 맞는 아이디를 추천해 주는 프로그램
#아이디 규칙은 
#길이가 3자 이상 15자 이하
#알파벳 소문자, 숫자, 뺴기(-), 밑줄(_), 마침표(.) 문자만 사용 가능
#단, 마침표(.)는 처음과 끝에 사용할 수 없고, 연속으로도 사용 불가

def solution(new_id):        
    
    #1단계 : 소문자 치환
    step_1 = new_id.lower()
    step_2 = ''
    #사용 불가한 특수문자
    special = ['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?',',','<','>','/']

    #2단계 : 소문자, 숫자, 뺴기, 밑줄, 마침표를 제외한 문자는 사용불가 
    for i in step_1 : 
        if i not in special :
            step_2 += i
    
    #3단계 : 마침표(.)가 2번 이상 연속된 위치면 하나로 표기
    step_3 = step_2[0]

    for i in range(1, len(step_2)) : 
        if step_2[i-1] == '.' and step_2[i] == '.' : 
            step_3 = step_3
        else : 
            step_3 += step_2[i]
    
    #4단계 : 처음과 끝에 마침표(.)가 위치하면 제거
    if step_3[0] == '.' and step_3[-1] == '.' :
        step_4 = step_3[1:-1]
    elif step_3[0] == '.' : 
        step_4 = step_3[1:]
    elif step_3[-1] == '.' : 
        step_4 = step_3[:-1]
    else : 
        step_4 = step_3
    
    #5단계 : 빈 문자열이면 a 대입
    if step_4 == '' :
        step_5 = 'a'
    else : 
        step_5 = step_4
    
    #6단계 : 길이가 16자 이상이면, 첫 15개의 문자만 사용
    if len(step_5) >= 15 : 
        step_6 = step_5[:15]
        if step_6[-1] == '.' : 
            step_6 = step_6[:-1]
    else : 
        step_6 = step_5

    #7단계 : 길이가 2자리 이하라면, 맨 마지막 문자를 길이가 3이 될 때까지 반복    
    while len(step_6) < 3 : 
        step_6 += step_6[-1]
    
    answer = step_6
    return answer

#테스트 케이스 정답은 "bat.y.abcdefghi"
print(solution("...!@BaT#*..y.abcdefghijklm"))
