import os
def print_file_name(path):
    files = os.listdir(path)
    for file in files:
        print(file)
    for file in files:
        if not file[-1] == ".":
            path = f"{path}/{file}"
            return print_file_name(path)
        else:
            print(file)

print_file_name("C:/Users/HP/Desktop/Moje programy/test")