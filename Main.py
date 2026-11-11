import os
import shutil
import shell,CPUs
#البداية من هنا
shell.shell()
CPUs.CPUs()  
def delete_folder ():
    print ("this function is working on delete the path of the folder that you'll push it . \n")
    print ("warning  the folder path that you will push  ,you will not able to recover it .\n    ")
    folder_path=input("push the folder path :  ")
    if os.path.exists(folder_path) :
        try:
            shutil.rmtree(folder_path)
            print(f"succeeded delete of : {folder_path} ")
        except Exception as e: 
            print(f"deletion failed *_* , be sure to close files in side it .\n (error detials :{e})")
    else  :
        print(f"I did not find the folder in path : {folder_path}")       
            
            