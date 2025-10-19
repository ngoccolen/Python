n1 = float(input("Nhập cạnh đầu tiên của tam giác: "))
n2 = float(input("Nhập cạnh thứ hai của tam giác: "))
n3 = float(input("Nhập cạnh thứ ba của tam giác: "))
if n1 == n2 == n3:
    print("Đây là tam giác đều")
elif n1 == n2 or n2 == n3 or n1 == n3:
    print("Đây là tam giác cân")
elif (n1 + n2 > n3) and (n1 + n3 > n2) and (n2 + n3 > n1):
    print("Đây là tam giác thường")
else:
    print("Ba cạnh trên không tạo thành tam giác")