#البدايه من هنا 
import os
import shutil
import shell,CPUs
shell.shell()
CPUs.CPUs() 
#I am abdullah bwoghaith  and this is my function 
#abdullah bwoghaith 
#(صورة ,مجلد ,ملف ....الخ)دالة تحدف اي مجلد مسار يمرر لها 
#import os #ما تحتاج شرح معروفة لنا قدها 
#import shutil #مكتبة الحدف اساس  الحدف 
def delete_folder ():# تعريف باسم الدالة
    print ("this function is working on delete the path of the folder that you'll push it . \n")#شرح لما تعمل علية الدالة
    print ("warning  the folder path that you will push  ,you will not able to recover it .\n    ")#تحدير المستخدم انه ما ما يقدر  يرجع الملف 
    folder_path=input("push the folder path :  ")
    if os.path.exists(folder_path) :
        try: #محاولة تنجنب الاخطاء مثلا لو الملف مفتوح ما ينهار البرنامج ادا ما قدر يحدفه
            shutil.rmtree(folder_path)#دالة الحدفة المستدعاة من  المكتبة الثانية
            print(f"succeeded delete of : {folder_path} ")
        except Exception as e: 
            print(f"deletion failed *_* , be sure to close files in side it .\n (error detials :{e})")#رسالة الخطاء ادا به
    else  :
        print(f"I did not find the folder in path : {folder_path}")     #في حال المجلد مو متواجد في المسار         
            
            