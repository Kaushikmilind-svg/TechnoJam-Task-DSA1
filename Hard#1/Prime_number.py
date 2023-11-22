a = int(input("Enter the first number : "))
b = int(input("Enter the last number : "))

prime_num = []

for num in range(a, b + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            prime_num.append(num)

print(f"Prime numbers between {a} and {b}:")
print(prime_num)
