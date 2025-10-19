def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i   
    return result
num = int(input("Nhập số cần tính giai thừa: "))
print(f"Giai thừa của {num} là: {factorial(num)}")
