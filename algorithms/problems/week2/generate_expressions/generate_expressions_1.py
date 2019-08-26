'''
practice generate expressions
'''

def generate_expression(arr,target):
    print(arr)
    arr.sort()
    res = ge_helper(arr,target,[[0,''],[1,''],['','']],[])
    return res

def ge_helper(arr,target,last,slate):
    if len(arr) == 1:
        return slate
    else:
        print(slate)
        print(last)
        one = arr[0]
        two = arr[1]
        arr = arr[2:]
        values = last[0]
        products = last[1]
        combs = last[2]
        v_last = values[0]
        v_str = values[1]
        p_last = products[0]
        p_str =  products[1]
        c_last = combs[0]
        c_str = combs[1]
        #for i in range(0,len(arr)-1):
        value = one + two + v_last
        product = one * two * p_last
        combination = int(str(one) + str(two) + c_last)
        #print(value)
        #print(combination)
        if combination == target:
            slate.append(c_str + str(combination))
        if value == target:
            slate.append(v_str + str(one) + '+' + str(two))
        if product == target:
            slate.append(p_str + str(one) + '*' + str(two))
        if value < target or product < target or combination < target:
            last = []
            last.append([value,str(one)+'+'+str(two)])
            last.append([product,str(one)+'*'+str(two)])
            last.append([combination,combination])
            print('call helper')
            ge_helper(arr,target,last,slate)
    return slate



arr1 = [2,2]
target = 4
r1 = generate_expression(arr1,target)
print(r1)
print('###############')
arr1 = [2,3]
target = 4
r1 = generate_expression(arr1,target)
print(r1)
print('###############')
arr1 = [3,4]
target = 34
r1 = generate_expression(arr1,target)
print(r1)
print('###############')
