def read_file(file):
    list_file = file.readlines()
    list_file.insert(0, str(file.name) + "\n")
    list_file.insert(1, str(len(list_file)-1) + "\n")
    return list_file

with open('1.txt', encoding='utf-8') as f1:
    list_file1 = read_file(f1)

with open('2.txt', encoding='utf-8') as f2:
    list_file2 = read_file(f2)

with open('3.txt', encoding='utf-8') as f3:
    list_file3 = read_file(f3)

list_all = [list_file1, list_file2, list_file3]
list_all.sort(key=len)

with open('Result.txt', 'a', encoding='utf-8') as f4:
    for list_any in list_all[0:-1]:
        f4.write("".join(list_any) + "\n")
    f4.write("".join(list_all[-1]))