'''
Nona Harris
CS-490-102
Professor McCann
06 February 2026

Calculate the greatest common divisor (GCD) of two integers a and by
using the Euclidean algorithm.
'''

def gcd(a: int, b: int) -> int:
    #In case of negative numbers
    a,b = abs(a), abs(b)

    #In the case of A and B being 0:
    if a == 0 and b == 0:
        print("Error: Negative value(s) ", end="")
        return None

    #In the case of A or B not being integers:
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Non-integer value(s) ", end="")
        return None
    
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    #Test Cases
    print(gcd(56, 49)) #Should return 7
    print(gcd(100, 90)) #Should return 10
    print(gcd(-4, -2)) #Should return 2
    print(gcd(7, 9)) #Should return 1
    print(gcd(2000, 4000)) #Should return 2000
    print(gcd(0, 9)) #Should return 9