'''
'''

def n_queens(n):

    col_used = [False] * n
    fwd_used = [False] * (2 * n - 1)
    bck_used = [False] * (2 * n - 1)

    def is_safe(row,col):
        return not (col_used[col] or fwd_used[col + row] or bck_used[col - row])

    def place_queens(board,row,res):
        if row == n:
            res.append([''.join(s) for s in board])
            return
        for col in range(n):
            #print('row ' + str(row) + ' col ' + str(col))
            if is_safe(row,col):
                board[row][col] = 'q'
                col_used[col] = True
                fwd_used[col + row] = True
                bck_used[col - row] = True
                place_queens(board,row+1,res)
                board[row][col] = '-'
                col_used[col] = False
                fwd_used[col + row] = False
                bck_used[col - row] = False
    res = []
    board = [['-'] * n for x in range(n)]
    place_queens(board,0,res)
    return res
print(n_queens(0))
print(n_queens(1))
print(n_queens(2))
print(n_queens(3))
print(n_queens(4))
print(n_queens(5))
print(n_queens(6))

'''
QUEEN = 'q'
NO_QUEEN = '-'

def find_arrangements(n):
    result = []
    board = []
    for i in range(0,n):
        row = []
        row.append(NO_QUEEN)
        for j in range(0,n):
            board.append(row)
    f_a_helper(board,0,n,result)

def f_a_helper(board,r,n,result):
    print(board)
    print(r)
    print(n)
    if r == n:
        result = board
        return
    while r < n:
        print(board[r])
        r = r + 1

    return result


n = 3
r1 = find_arrangements(n)
print(r1)
