chuoi_nhap = input("Nhập các số: ")
ds_chuoi = chuoi_nhap.split(",")
ds_le = [] 
for x in ds_chuoi:           
    so = int(x)              
    if so % 2 != 0:         
        ds_le.append(so)
print("Các số lẻ là:", ds_le)
