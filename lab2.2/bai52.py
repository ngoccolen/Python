def is_perfect_number(n):
    if n <= 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n
print("Các số hoàn hảo từ 1 đến 10.000 là:")
for num in range(1, 10001):
    if is_perfect_number(num):
        print(num)