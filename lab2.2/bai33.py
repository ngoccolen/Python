str = input("Nhập 1 chuỗi: ")
str = str.replace(" ", "").lower()
palindrome = True
for i in range(len(str) // 2):
    if str[i] != str[len(str) - i - 1]:
        palindrome = False
        break
if palindrome:
    print("Đây là chuỗi palindrome")
else:
    print("Đây không phải chuỗi palindrome")