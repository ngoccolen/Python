def is_good_password(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
    return has_upper and has_lower and has_digit
pw = input("Nhập mật khẩu cần kiểm tra: ")
if is_good_password(pw):
    print("Mật khẩu tốt.")
else:
    print("Mật khẩu chưa đủ mạnh.")
