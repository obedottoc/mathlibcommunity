import math
class NumberSystem:
    def to_binary(n):
        """
        Convert decimal to binary
        """
        return bin(n).replace("0b", "")


    def to_decimal(b):
        """
        Convert binary to decimal
        """
        return int(b, 2)


    def to_hexadecimal(n):
        """
        Convert decimal to hexadecimal
        """
        return hex(n).replace("0x", "").upper()

 
    def to_octal(n):
        """
        Convert decimal to octal
        """
        return oct(n).replace("0o", "")