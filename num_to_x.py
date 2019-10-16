# convert a decimal number to other formats
import math
num = int(input("enter the number to convert: "))

# reverse the string (the numbers are read in reverse
# when conveting via division)


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


def to_binary(num):
    binary = ''
    while num >= 1:
        rem = num % 2  # we get only 0, 1
        binary = binary + str(math.floor(rem))  # append to string
        num = num / 2
    binary = binary + 'b0'  # append the binary identifier
    binary = reverse_str(binary)
    return binary


def to_hex(num):
    hexdemical = ''
    while num >= 1:
        rem = num % 16
        hexdemical = hexdemical + str(math.floor(rem))
        num = num / 16
    hexdemical = hex_not(hexdemical)
    hexdemical = hexdemical + 'x0'
    hexdemical = reverse_str(hexdemical)
    return hexdemical


def to_oct(num):
    octal = ''
    while num >= 1:
        rem = num % 8
        octal = octal + str(math.floor(rem))
        num = num / 8
    octal = octal + 'o0'
    octal = reverse_str(octal)
    return octal


print(num, "in binary is: ", to_binary(num))
print(num, "in hexdemical is: ", to_hex(num))
print(num, "in octal is: ", to_oct(num))
