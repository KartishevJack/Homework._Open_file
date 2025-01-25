import os

list_changed_files = []

def read_file(file_):
    list_str = file_.readlines()
    list_str.insert(0, str(file_.name) + "\n")
    list_str.insert(1, str(len(list_str)-1) + "\n")
    return list_str

for file in os.listdir("."):
    if file.endswith(".txt") and os.path.basename(file) != "Result.txt":
        with open(file, encoding='utf-8') as f:
            list_changed_files.append(read_file(f))

list_changed_files.sort(key=len)

with open('Result.txt', 'a', encoding='utf-8') as f1:
    if len(list_changed_files) > 1:
        for list_any in list_changed_files[0:-1]:
            f1.write("".join(list_any) + "\n")
        f1.write("".join(list_changed_files[-1]))
    elif len(list_changed_files) == 1:
        f1.write("".join(list_changed_files[0]))