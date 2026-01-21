"""
PROBLEM: Implement an integer to string conversion function, and a string to integer conversison function.
For example, if the input to the first function is the integer 314, it should return the string “314” and
if the input to the second function is the string “314” it should return the integer 314.

Hint: Build the result one digit at a time. 
"""

def int_to_string(x):
    # Handle zero explicitly
    if x == 0:
        return "0"

    is_negative = False
    if x < 0:
        is_negative = True
        x = -x  # make it positive

    digits = []

    # Extract digits
    while x > 0:
        digit = x % 10
        digits.append(chr(ord('0') + digit))
        x //= 10

    # Reverse digits and add sign if needed
    result = ''.join(reversed(digits))
    return '-' + result if is_negative else result


# string to integer

def string_to_int(s):
    is_negative = False
    start_index = 0

    if s[0] == '-':
        is_negative = True
        start_index = 1

    result = 0

    for i in range(start_index, len(s)):
        digit = ord(s[i]) - ord('0')
        result = result * 10 + digit

    return -result if is_negative else result 

# time complexity = 0(n) number of digits
# space complexity = 0(n) digit storage

# time complexity = 0(n)
# space compexity = 0(1)