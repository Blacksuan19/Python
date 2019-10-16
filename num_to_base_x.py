# convert a decimal number to any provided base
import math
num = int(input("enter decimal number to convert: "))
base = int(input("enter base to convrt number to: "))


def reverse_str(string):
    return string[::-1]


def hex_not(hexi):
    hexi = hexi.replace('10', 'a')
    hexi = hexi.replace('11', 'b')
    hexi = hexi.replace('12', 'c')
    hexi = hexi.replace('13', 'd')
    hexi = hexi.replace('14', 'e')
    hexi = hexi.replace('15', 'f')
    return hexi


def num_to_base_x(num, base):
    final = ''
    while num >= 1:
        rem = num % base
        final = final + str(math.floor(rem))
        num = num / base
    # prefixes for known bases
    if base == 2:
        final = final + 'b0'
    if base == 8:
        final = final + 'o0'
    if base == 16:
        final = final + 'x0'
        final = hex_not(final)
    final = reverse_str(final)
    return final


print(num, "in base", base, "is:", num_to_base_x(num, base))
