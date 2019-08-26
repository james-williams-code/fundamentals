'''
implement n queens

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
