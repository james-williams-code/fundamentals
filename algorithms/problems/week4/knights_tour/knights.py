'''

'''
from collections import deque
def knights_path(rows,cols,start_row,start_col,end_row,end_col):

    directions = [(2,1),(2,-1),(-2,-1),(-2,1),(1,2),(-1,2),(-1,-2),(1,-2)]

    def get_neighbors(r, c):
        neighbors = []
        for dr,dc in directions:
            new_r, new_c = dr + r, dc + c
            if new_r >= 0 and new_r <rows and new_c >= 0 and new_c < cols:
                neighbors.append((new_r,new_c))
        return neighbors


    start_cell = start_row, start_col

    visited = {start_cell}

    q = deque([(start_cell,0)])

    while q:
        cell, count = q.popleft()
        print(cell)
        print(count)
        if cell == (end_row,end_col):
            return count

        for new_cell in get_neighbors(cell[0], cell[1]):
            print(q)
            if new_cell not in visited:
                q.append((new_cell,count+1))
                visited.add(new_cell)
    return -1

print(knights_path(5,5,0,0,4,1))

