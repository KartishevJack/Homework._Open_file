import os

list_files_names = []
list_lists_changed_files = []

for file in os.listdir("."):
    if file.endswith(".txt"):
        list_files_names.append(file)

def read_file(file):
    list_str = file.readlines()
    list_str.insert(0, str(file.name) + "\n")
    list_str.insert(1, str(len(list_str)-1) + "\n")
    return list_str

for file_name in list_files_names:
    with open(file_name, encoding='utf-8') as f:
        list_lists_changed_files.append(read_file(f))

list_lists_changed_files.sort(key=len)

with open('Result.md', 'a', encoding='utf-8') as f1:
    for list_any in list_lists_changed_files[0:-1]:
        f1.write("".join(list_any) + "\n")
    f1.write("".join(list_lists_changed_files[-1]))