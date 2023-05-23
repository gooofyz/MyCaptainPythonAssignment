import csv
def write_in_file(info_list):
    with open("student_info.csv","a+",newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","RollNo","Phno","Email id"])
        writer.writerow(info_list)
if __name__ == "__main__":
    condition=1
    student=1
    while condition== 1:
        student_info=input("Enter the student#{} details in format\n(Name,RollNo,Phno,Email id): ".format(student))
        student_info_list=student_info.split(",")
        print("\nEntered student#{} details are- \nName: {}\nRollNo: {}\nPhno: {}\nEmail id: {}"
              .format(student,student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice=input("Is the entered info correct(Y/N): ")
        if choice.capitalize()=="Y":
            write_in_file(student_info_list)
            student+=1
            condition_check=input("do you want to add another student details(Y/N) : ")
            if condition_check.capitalize()== "Y":
                condition=1
            else:
                condition=0
        elif choice.capitalize()=="N":
            print("Please re-enter the values")
