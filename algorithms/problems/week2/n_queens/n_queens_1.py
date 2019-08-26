'''
Implement the n-queens problem
'''
QUEEN='q'

def find_arrangements(n):
    print(n)
    f_a_util([],[],n,0)

def f_a_util(chessboard, result, n, row):
    if n == 0:
        result = chessboard
        return
    else:
        for col in range(0,n):
            if is_safe(chessboard, row, col, n):
                chessboard[row][col] = 'Q'
                f_a_util(chessboard,result,n,row+1)
                chessboard[row][col] = '-'

def is_safe(chessboard,row,column,n):
    curr_col = column
    curr_row = row
    while curr_row >= 0 and curr_col >= 0:
        if chessboard[curr_row-1][curr_col-1] == 'Q':
            return False
    curr_row = row
    while curr_row >= 0:
        if chessboard[curr_row-1][curr_col] == 'Q':
            return False
    curr_row = row
    curr_col = column
    while curr_row >=0 and curr_col < n:
        if chessboard[curr_row-1][curr_col+1] == 'Q':
            return False
    return True



n1 = 1
find_arrangements(n1)
