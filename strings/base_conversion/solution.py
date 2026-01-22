"""
PROBLEM: Write a program that performs base conversion. The input is a string, an integer b;,
and another integer b7. The string represents an integer in base b;. The output should be the
string representing the integer in base b7. Assume 2 < bi,b2 < 16. Use “A” to represent 10,
“B” for 11,..., and “F” for 15. (For example, if the string is “615”, b; is 7 and bz is 13,
then the result should be “1A7”, since 6x77 +1xX7+5=1x 13* +10 13+7.)

Hint: What base can you easily convert to and from? 
"""

from math import remainder


class Solution:
    def convert_base(self, num_as_string: str, b1: int, b2: int) -> str:
        # Handle negative numbers
        is_negative = num_as_string[0] == '-'
        if is_negative:
            num_as_string = num_as_string[1:]

        # Step 1: Convert from base b1 to integer
        num_as_int = 0
        for char in num_as_string:
            if '0' <= char <= '9':
                digit = ord(char) - ord('0')
            else:
                digit = ord(char.upper()) - ord('A') + 10

            num_as_int = num_as_int * b1 + digit

        # Step 2: Convert integer to base b2
        if num_as_int == 0:
            result = "0"
        else:
            digits = []
            while num_as_int > 0:
                remainder = num_as_int % b2
                if remainder < 10:
                    digits.append(chr(ord('0') + remainder))
                else:
                    digits.append(chr(ord('A') + remainder - 10))
                num_as_int //= b2

            result = ''.join(reversed(digits))

        # Step 3: Add negative sign if needed
        return '-' + result if is_negative else result