import os
#EDIT FUNCTION
def edit_file():
    path = input('File Path: ')
    if os.path.exists(path):
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
    else:
        print('File does not exist')