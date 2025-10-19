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
text = input("Nhập chuỗi cần mã hóa: ")
mahoa_chuoi = mahoa(text)
print("Chuỗi sau khi mã hóa:", mahoa_chuoi)