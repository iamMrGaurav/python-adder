from inputs import convert_binary

"""
This is binary 8 bit adder

"""
def half_adder(a, b):
    sum__ = a^b 
    carry = a and b 
    return sum__, carry

def full_adder(a, b, carry_in):
    sum1, carry1 = half_adder(a, b)
    sum_, carry2 = half_adder(sum1, carry_in)
    carry = carry1 or carry2
    return sum_, carry


def adder():
    first_value, second_value = convert_binary()
    c_in = 0
    fin = []

    for i in range(len(first_value)-1, -1, -1):
        add, c_in = full_adder(first_value[i], second_value[i], c_in)
        fin.insert(0, add)
    fin.insert(0, c_in)

    fin = int("".join(str(i) for i in fin))
    print("Result is : ", fin)

