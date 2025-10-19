m = input("Nhap thang: ").lower()
if m in ['january', 'march', 'may', 'july', 'august', 'october', 'december']:
    print(m, "co 31 ngay")
elif m in ['april', 'june', 'september', 'november']:
    print(m, "co 30 ngay")
elif m == 'february':
    print(m, "co 28 hoac 29 ngay")
else:
    print("Khong hop le")