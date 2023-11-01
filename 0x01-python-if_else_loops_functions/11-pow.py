#!/usr/bin/python3
from decimal import Decimal

def pow(a, b):
    a = Decimal(str(a))
    b = Decimal(str(b))
    if b == 0:
        return 1
    if b < 0:
        a = Decimal(1) / a
        b = -b
    result = Decimal(1)
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result
