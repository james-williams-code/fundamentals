'''
'''

def print_wildcard_permutations(s):

    n = len(s)

    output = []
    possible = ['0','1']
    def print_helper(perm,pos):
        if pos == n:
            output.append(perm)
            return
        if s[pos] == '?':
            for p in possible:
                st = perm + p
                print_helper(st,pos+1)
        else:
            perm += s[pos]
            print_helper(perm, pos + 1)
    print_helper('',0)
    return output

s1 = '?a'
print(print_wildcard_permutations(s1))
s2 = 'a?a?'
print(print_wildcard_permutations(s2))


