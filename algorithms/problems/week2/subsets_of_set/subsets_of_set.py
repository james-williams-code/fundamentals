'''
return the subsets of a set
'''

def subsets(s):
    print(s)
    subsets = []
    subsets_helper(subsets,s,0,'')
    return subsets

def subsets_helper(subsets,s,pos,c_subset):
    #print(pos)
    #print(len(s))
    if pos == len(s):
        subsets.append(c_subset)
        return
    subsets_helper(subsets,s,pos + 1,c_subset)
    subsets_helper(subsets,s,pos + 1,c_subset + s[pos])

arr1 = ['a','b']
r1 = subsets(arr1)
print(r1)

arr2 = ['z','y','x','v','u','t']
r2 = subsets(arr2)
print(r2)

