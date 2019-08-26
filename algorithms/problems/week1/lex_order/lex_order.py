def lex_order(arr):
    keys = {}
    count = {}
    res = []
    for i in range(0,len(arr)):
        item = arr[i].split()
        key = item[0]
        value = item[1]
        print(key)
        print(value)
        if key not in keys:
            keys[key] = value
        elif value > keys[key]:
            keys[key] = value
        if key not in count:
            count[key] = 1
        else:
            count[key] = count[key] + 1
    for key in keys:
        res.append(key + ':' + str(count[key]) + ',' + keys[key])
    return res

arr1 = ['key1 value1', 'key2 value2', 'key1 zvalue']
r1 = lex_order(arr1)
print(r1)
