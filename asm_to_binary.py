import textwrap
'''
simple assmebly instruction to binary converter by blacksuan19

Instruction binary structure for types:

R type:
    add $t0, $t1, $t2
    $t0 = $t1 + $t2
           |       |   $t1  |   $t2  |   $t0  |       |   add   |
           | OP(6) |  RS(5) |  RT(5) |  RD(5) | SA(5) | Func(6) |


'''
# TODO ask about the type before asking for input
# TODO process each input in a diff function
# TODO hardcode the addresses of each register


def instruction_to_bin(ins):
    '''replace the instruction in text whith its binary
    equivalent (based on mips arch, )'''
    ins = ins.replace('add',  '100000')
    ins = ins.replace('addu',  '100001')
    ins = ins.replace('addi',  '001000')
    ins = ins.replace('addiu',  '001001')
    ins = ins.replace('and',  '100100')
    ins = ins.replace('andi',  '001100')
    ins = ins.replace('div',  '011010')
    ins = ins.replace('divu',  '011011')
    ins = ins.replace('mult',  '011000')
    ins = ins.replace('multu',  '011001')
    ins = ins.replace('nor',  '100111')
    ins = ins.replace('or',  '100101')
    ins = ins.replace('ori',  '001101')
    ins = ins.replace('sll',  '000000')
    ins = ins.replace('sllv',  '000100')
    ins = ins.replace('sra',  '000011')
    ins = ins.replace('srav',  '000111')
    ins = ins.replace('srl',  '000010')
    ins = ins.replace('srlv',  '000110')
    ins = ins.replace('sub',  '100011')
    ins = ins.zfill(6)  # make it 6 bits cuz thats how it should be
    return ins


def register_to_address(register):
    '''function to convert the given register to binary
        address according to mips architecture'''
    switcher = {
        "zero": 0,
        "0": 0,
        "at": bin(1),
        "v0": bin(2),
        "v1": bin(3),
        "a0": bin(4),
        "a1": bin(5),
        "a2": bin(6),
        "a3": bin(7),
        "t0": bin(8),
        "t1": bin(9),
        "t2": bin(10),
        "t3": bin(11),
        "t4": bin(12),
        "t5": bin(13),
        "t6": bin(14),
        "t7": bin(15),
        "s0": bin(16),
        "s1": bin(17),
        "s2": bin(18),
        "s3": bin(19),
        "s4": bin(20),
        "s5": bin(21),
        "s6": bin(22),
        "s7": bin(23),
        "t8": bin(24),
        "t9": bin(25),
        "k0": bin(26),
        "k1": bin(27),
        "gp": bin(28),
        "sp": bin(29),
        "fp": bin(30),
        "ra": bin(31)
           }
    '''remove the 0b prefix first and make it 5 bits'''
    return str(switcher.get(register)).replace("0b", "").zfill(5)


def bin_to_hex(bin_str):
    '''covert a given 32bit string to hex'''
    splitted_str = textwrap.fill(bin_str, 4)  # split to 4 places
    splitted_str = splitted_str.split("\n")  # convert it to a list
    splitted_hex = []
    final_str = ""
    for string in splitted_str:  # convert it to a hex list
        splitted_hex.append(hex(int(string, 2))[2:])
    for hexi in splitted_hex:
        final_str = final_str + hexi
    final_str = "0x" + final_str
    return final_str


if __name__ == "__main__":
    '''main function starts here'''
    instruction = input("enter the instruction: ")
    Rs = input("enter Rs (the term in the middle usually): ")
    Rt = input("enter Rt (the last term usually): ")
    Rd = input("enter Rd (the register you're saving to): ")
    bin_Rs = register_to_address(Rs)
    bin_Rt = register_to_address(Rt)
    bin_Rd = register_to_address(Rd)
    bin_ins = instruction_to_bin(instruction)
    # the empty places are supposed to be filled by zeros
    bin_rep = "".zfill(6) + bin_Rs + bin_Rt + bin_Rd + "".zfill(5) + bin_ins
    print("\nthe instruction is: %s $%s, $%s, $%s" % (instruction, Rd, Rs, Rt))
    print("the binary representation is: ", bin_rep,
          "\nthe hex representation is: ", bin_to_hex(bin_rep))
