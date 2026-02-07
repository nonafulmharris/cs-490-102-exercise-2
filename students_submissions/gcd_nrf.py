'''

Nona Harris
CS-490-102
Professor McCann
06 February 2026

gcd_nrf.py:
    - Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.

'''

def gcd(a: int, b: int) -> int:
    #In the case of negative numbers
    if a < 0 or b < 0:
        print("Error: Negative value(s) ", end="")
        return None

    if b == 0:
        return a
    return gcd(b, a % b)

#Test Cases
print(gcd(56, 49)) #Should return 7
print(gcd(100, 90)) #Should return 10
print(gcd(-4, -2)) #Should print Error message
print(gcd(7, 9)) #Should return 1
print(gcd(2000, 4000)) #Should return 2000
print(gcd(0, 9)) #Should return 9
