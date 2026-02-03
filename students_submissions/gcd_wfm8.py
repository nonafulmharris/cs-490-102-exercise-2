def gcd(a: int, b: int) -> int:

    return a if a < b else b


# Test cases
print(gcd(54, 24))  # Expected output: 24
print(gcd(48, 18))  # Expected output: 18
print(gcd(101, 10))  # Expected output: 10