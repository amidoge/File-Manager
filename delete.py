import os
#DELETE FUNCTION
def delete_file():
    path = input('File Path: ')
    if os.path.exists(path):
        os.remove(path)
    else:
        print('File does not exist')