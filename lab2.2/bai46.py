def print_last5_squares():
    squares = []
    for i in range(1, 21):
        squares.append(i ** 2)
    print("5 phần tử cuối cùng là:", squares[-5:])  

print_last5_squares()
