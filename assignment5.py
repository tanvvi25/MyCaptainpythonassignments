# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 17:24:10 2023

@author: USER
"""
import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'w+','newline') as csv_false:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            
            writer.writer("Name", "Age","Contact_no","Email Id")
        
        writer.writer(info_list)
        
if __name__ == '__main__':  



condition = True
student_num = 1

while(condition):
    student_info = input("Enter student information for student in the following format (Name Age Contact_Number E-mail_Id"):".format(student_name))
    print("Entered information" + student_info)
    
    # split
    student_info_list = student_info.split('')
    print("Entered split up information is:" + str(student_info_list))
    
    print("\nThe entered information is -\nName: {}\nAge:{}\nContact_number:{}\nE-mail\ID:{}"
          .format(student_info_list[0],student_info_list[1],student_info_list[2],student-info_list[3]))
    print("Is the entered information correct? (yes/no):")
    
    if choice_check =="yes":
       write_into_csv(student_info_list)
       
       condition_check = input("Enter (yes/no") if you want to enter information for another students:")
    if condition_check =="yes":
    condition = True
    student_num = student_num + 1
    elsecondition_check =="no":
    condition = False
elif choice_check == "no":
    print("\nPlease re-enter the values!")
    
    