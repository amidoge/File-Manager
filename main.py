#CREATE FUNCTION
def create(default_path):
    file_name = input('File Name: ')
    path = input('File Location: ') 
    if path == "":
        path = default_path 
    if ".txt" in file_name:
        file = open(path + file_name, "x")
    else:
        file = open(path + file_name + ".txt", "x")
    file.close()
#EDIT FUNCTION
def edit():
    path = input('File Path: ')
    b = int(input("Press...\n- (1) to read a file \n- (2) to write in a file\n"))
    if b == 1:
        file = open(path, "r")
        print(file.read())
        file.close()
    elif b == 2:
        file = open(path, "a")
        text = input('Write below...\n')
        file.write(text)
        file.close()
#MAIN CONDITION
if __name__ == '__main__':
    default_path = "C:/Users/Amito/Desktop/File Manager/"
    a = int(input("Press...\n- (1) to create a new file? \n- (2) to read/write a file \n- (3) to delete a file \n"))
    #CREATE
    if a == 1:
        create(default_path)
    #EDIT
    if a == 2:
        edit()
    #DELETE