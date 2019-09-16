'''
'''
class disk():

    def __init__(self,value):
        self.value = value

def place_disks(n):
    answer = []

    def disk_helper(n,from_peg,to_peg,aux_peg):
        if n == 1:
            answer.append((from_peg,to_peg))
            return
        disk_helper(n-1,from_peg,aux_peg,to_peg)
        answer.append((from_peg,to_peg))
        disk_helper(n-1,aux_peg,to_peg,from_peg)
    disk_helper(n,1,3,2)
    return answer

print(place_disks(4))
