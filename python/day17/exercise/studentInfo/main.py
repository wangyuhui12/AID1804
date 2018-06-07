
from menu import *
from student_info import *

def main():
    L = []
    f = Student()
    while True:
        menu()
        s = input("请选择：")
        if s == '1':
            L = f.input_student()
            f.set_L(L)
        elif s == '2':
            f.output_student()
        elif s == '3':
            f.change_student()
        elif s == '4':
            f.delete_student()
        elif s == '5':
            f.scoreHighToLow()
        elif s == '6':
            f.scoreLowToHigh()
        elif s == '7':
            f.ageOldToYoung()
        elif s == '8':
            f.ageYoungToOld()
        elif s == '9':
            f.student_info_save()
        elif s == '10':
            f.student_info_read()

        else:
            break

if __name__ == '__main__':
    main()