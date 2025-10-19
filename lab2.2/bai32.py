def mahoa(text,shift=3):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result
def giai_ma(text,shift=3):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result
text1 = input("Nhập chuỗi cần mã hóa: ")
text2 = input("Nhập chuỗi cần giải mã: ")
mahoa_chuoi = mahoa(text1)
print("Chuỗi sau khi mã hóa:", mahoa_chuoi)
giaima_chuoi = giai_ma(mahoa_chuoi)
print("Chuỗi sau khi giải mã:", giaima_chuoi)