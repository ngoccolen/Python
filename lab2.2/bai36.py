ds_so = []
print("Nhập các số nguyên (nhập 0 để kết thúc):")
while True:
    n = int(input("Nhập số: "))
    if n == 0:
        break  
    ds_so.append(n)  
ds_so.sort()
print("Các số đã nhập (theo thứ tự tăng dần):")
for so in ds_so:
    print(so)