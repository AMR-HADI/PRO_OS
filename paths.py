import os
def change_directory():
    new_path = input("enter the new path: ")

    try:
        os.chdir(new_path)
        print("Directory changed successfully !")
        print("Current path: ",os.getcwd())
    except FileNotFoundError:
        print("Error: Path does not exist.")

    except NotADirectoryError:
        print("Error: The Path is not a directory.")