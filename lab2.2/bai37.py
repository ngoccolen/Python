ds_tu = []
print("Nhập từng từ (nhấn Enter trên dòng trống để kết thúc):")
while True:
    tu = input()
    if tu == "":  
        break
    if tu not in ds_tu:
        ds_tu.append(tu)
for t in ds_tu:
    print(t)
