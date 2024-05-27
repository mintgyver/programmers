#데이터가 [코드번호(code), 제조일(date), 최대 수량(maximum), 현재수량(remain)] 으로 구성되어 있습니다.
#이 데이터중 조건을 만족하는 데이터를 뽑아서 오름차순으로 정렬하고자 합니다.
#어떠한 정보를 기준으로 데이터를 뽑을지 정하는 문자열 "ext"
#뽑아낼 정보의 기준값을 나타내는 정수 "val_ext"
#정보를 정렬할 기준이 되는 문자열 "sort_by" 입니다.
#data에서 ext값이 val_ext보다 작은 데이터만을 뽑은 후 sort_by에 해당하는 값을 기준으로 오름차순

def solution(data, ext, val_ext, sort_by):
    
    data_check = ["code", "date", "maximum", "remain"]      #기준값 문자열 리스트
    len_data = len(data)
    data_sort = []    
    ext_num = data_check.index(ext)                         #문자열 ext에 해당하는 index 추출
    sort_num = data_check.index(sort_by)                    #문자열 sort_by에 해당하는 index 추출
            
    for i in range(0,len_data) : 
        if data[i][ext_num] < val_ext :                     #val_ext보다 작은 값만 추출
            data_sort.append(data[i])

    data_sort.sort(key=lambda x:x[sort_num])                #다차원배열 정렬
            
    return data_sort

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))
#정답은 [[3, 20300401, 10, 8], [1, 20300104, 100, 80]]