def print_except_first5():
    squares = []
    for i in range(1, 21):
        squares.append(i ** 2)
    print("Danh sách trừ 5 phần tử đầu:", squares[5:])  
print_except_first5()
