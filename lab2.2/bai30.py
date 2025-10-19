str1 = int(input("Nhập năm: "))
if str1 % 4 == 0 and str1 % 100 != 0 or str1 % 400 == 0:
    print(str1, "là năm nhuận")
elif str1 > 0:
    print(str1, "không phải là năm nhuận")
else:
    print("Năm không hợp lệ")