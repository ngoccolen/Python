ds_so = []
print("Nhập các số nguyên (nhấn Enter trên dòng trống để kết thúc):")
while True:
    so = input()
    if so == "":  
        break
    ds_so.append(so)
negatives = []  
zeros = []      
positives = []  
for n in ds_so:
    if n < 0:
        negatives.append(n)
    elif n == 0:
        zeros.append(n)
    else:
        positives.append(n)

result = negatives + zeros + positives
print("Kết quả sau khi sắp xếp theo quy tắc:")
for t in ds_so:
    print(t)
