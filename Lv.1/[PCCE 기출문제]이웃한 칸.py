#각 칸마다 색이 칠해진 2차원 격자 보드판이 있습니다.
#그 중 한칸을 골랐을 때, 위, 아래, 왼쪽, 오른쪽 칸 중 같은 색깔로 칠해진 칸의 개수를 구하려고 합니다.

def solution(board, h, w):
    
    count = 0                               #같은 색의 갯수를 저장할 count
    h_check, w_check  = 0, 0                #수평, 수직으로 check할 칸을 나타내는 변수
    dh = [0, 1, -1, 0]                      #해당 칸의 위 아래를 체크하기 위한 리스트
    dw = [1, 0, 0, -1]                      #해당 칸의 왼쪽, 오른쪽을 체크하기 위한 리스트
    
    for i in range(0,4) : 
        h_check = h +dh[i]                  #dh, dw에 따라 주변의 칸을 체크
        w_check = w +dw[i]
        if 0 <= h_check < len(board) :      #정해진 칸을 벗어나서는 체크하지 않는다.
            if 0 <= w_check < len(board) :
                if board[h][w] == board[h_check][w_check] : 
                    count += 1
                    
    return count

print(solution(	[["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1))
#정답은 2