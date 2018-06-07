
from menu import menu
from student_info import *  

def main():
    L = []
    while True:
        menu()
        s = input("请选择：")
        if s == '1':
            L += input_student()
        elif s == '2':
            output_student(L)
        elif s == '3':
            change_student(L)
        elif s == '4':
            delete_student(L)
        else:
            break

            
if __name__ == '__main__':
    main()