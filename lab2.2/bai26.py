def docchucai(x):
    if x in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        print(x, "là nguyên âm")
    elif x == 'y':
        print(x, "co the la phu am, co the la nguyen am")
    else:
        print(x, "là phụ âm")
x = input("Nhập vào một ký tự: ")
docchucai(x)