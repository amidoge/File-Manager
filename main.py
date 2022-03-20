import create
import edit
import delete
#MAIN CONDITION
if __name__ == '__main__':
    default_path = "C:/Users/Amito/Desktop/File Manager/"
    a = int(input("Press...\n- (1) to create a new file? \n- (2) to read/write a file \n- (3) to delete a file \n"))
    #CREATE
    if a == 1:
        create.create_file(default_path)
    #EDIT
    if a == 2:
        edit.edit_file()
    #DELETE
    if a == 3:
        delete.delete_file()