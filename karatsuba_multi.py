import math


# Function for Zeropadding

def zeroPad(a, param):
    return a * math.pow(10, param)


# Function For splitting the number

def split_digit(a, b, j, flag):
    l1 = []
    l2 = []
    ten = math.pow(10, j)

    value = a
    if value == 0:
        l1.append(0)
    while value > 0:
        digit = value % ten
        l1.append(digit)
        value = math.floor(value / ten)
    if flag:  # Appending zeros if flag is set
        l1.append(0)

    value = b
    if value == 0:
        l2.append(0)
    while value > 0:
        digit = value % ten
        l2.append(digit)
        value = math.floor(value / ten)
    if flag:  # Appending zeros if flag is set
        l2.append(0)

    b = l1[0]
    a = l1[1]
    d = l2[0]
    c = l2[1]
    return a, b, c, d


# Function for karatsuba multiplication.
def k_multiply(a, b):
    set_offset_first_flag = False  # Flag for setting offset when number of digits is less in a compare to b
    set_offset_second_flag = False  # Flag for setting offset when number of digits is less in b compare to a
    pad_digit_flag = False  # Flag for appending leading zeros.

    if digit_length(a) == 1 and digit_length(b) == 1: # Direct Multiplication for single digits
        return a * b;

    if digit_length(a) < digit_length(b):
        pad_digit_flag = True
        set_offset_first_flag = True
        offset = digit_length(b) - digit_length(a)

    elif digit_length(b) < digit_length(a):
        pad_digit_flag = True
        set_offset_second_flag = True
        offset = digit_length(a) - digit_length(b)

    if pad_digit_flag and set_offset_first_flag:
        n = digit_length(a) + offset

    elif pad_digit_flag and set_offset_second_flag:
        n = digit_length(b) + offset

    else:
        n = digit_length(a)

    j = n // 2

    if (n % 2) != 0:
        n += 1
        j += 1

    nby2_padding = j
    n_padding = n

    a, b, c, d = split_digit(a, b, j, pad_digit_flag)

    ac = k_multiply(a, c)
    bd = k_multiply(b, d)
    res1 = a + b
    res2 = c + d
    k = k_multiply(res1, res2)

    A = zeroPad(ac, n_padding)
    B = zeroPad(k - ac - bd, nby2_padding)

    return A + B + bd


def digit_length(a):
    if a > 0:
        digits = int(math.log10(a)) + 1
    elif a == 0:
        digits = 1
    return digits


print(k_multiply(10, 20))

# Equation for karatsuba multiplication is [10^n.ac+{(a+b)(c+d)-ac-bd}.10^(n/2)+bd]
# Function call is recursive in nature.