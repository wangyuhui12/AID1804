
# with open('info.txt') as f:
#     print(f.read())

try:
    f = open('info.txt')
    print(f.read())
    # while True:
    #     F = f.readline()
    #     print(F, end='')
    #     if F == '':
    #         break
    f.close()
except OSError:
    print("文件读取失败")


