def all_sublists(lst):
    sublists = []
    n = len(lst)
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            sublists.append(lst[i:j])
    sublists.append([])  
    return sublists
data = [1, 2, 3]
print("Danh sách con của", data, "là:")
for sub in all_sublists(data):
    print(sub)
