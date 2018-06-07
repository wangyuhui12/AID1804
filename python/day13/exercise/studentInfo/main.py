
from menu import *
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
        elif s == '5':
            scoreHighToLow(L)
        elif s == '6':
            scoreLowToHigh(L)
        elif s == '7':
            ageOldToYoung(L)
        elif s == '8':
            ageYoungToOld(L)
        elif s == '9':
            student_info_save(L)
        elif s == '10':
            student_info_read()

        else:
            break

if __name__ == '__main__':
    main()