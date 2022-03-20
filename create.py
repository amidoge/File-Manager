#CREATE FUNCTION
def create_file(default_path):
    file_name = input('File Name: ')
    path = input('File Location: ') 
    if path == "":
        path = default_path 
    if ".txt" in file_name:
        file = open(path + file_name, "x")
    else:
        file = open(path + file_name + ".txt", "x")
    file.close()