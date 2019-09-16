'''
'''


def raise_to_the_power_of(n,e):

    output = []
    def power(total,e):
        if e == 1:
            total = total * n
            output.append(total)
            return total
        power(total * n, e - 1)
    power(1,e)
    return output

print(raise_to_the_power_of(2,10))
