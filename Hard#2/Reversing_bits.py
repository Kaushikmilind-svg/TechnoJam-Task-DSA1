def rev_bits(n):
    bin_str = bin(n)[2:][::-1]

    revd_bits = int(bin_str, 2)

    return revd_bits

# Example:
# Input: 10 (binary representation: 1010)
# Output: 5 (binary representation after reversing: 0101)
input_number = int(input("Enter a non-negative integer: "))
result = rev_bits(input_number)

print("The number obtained is : " , result)
