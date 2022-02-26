#CREATE FUNCTION
def create(default_path):
    file_name = input('File Name: ')
    path = input('Folder Name: ') 
    if path == "":
        path = default_path 
    if ".txt" in file_name:
        file = open(path + file_name, "x")
    else:
        file = open(path + file_name + ".txt", "x")

#MAIN CONDITION
if __name__ == '__main__':
    default_path = "C:/Users/Amito/Desktop/File Manager/"
    a = int(input("Press...\n- (1) to create a new file? \n- (2) to edit a file \n- (3) to delete a file \n"))
    #CREATE
    if a == 1:
        create(default_path)
    #EDIT