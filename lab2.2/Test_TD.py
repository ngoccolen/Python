from tu_dien import *
max=int(input("Nhap gia tri lon nhat: "))
TD=Tao_TD(max)
print("In tat ca cac phan tu trong tu dien: ")
Print_Item(TD)
print("In tat ca cac khoa trong tu dien: ")
Print_key(TD)
print("In tat ca cac gia tri trong tu dien: ")
Print_value(TD)