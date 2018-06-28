import  re 
import sys 

def get_address(port):
    #提取port对应的段落
    pattern = r'\S+'
    
    f = open('1.txt') 
    while True:
        #提取每一段
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        if not data:
            return "Sorry not found" 
        #查找首个但是是不是指定端口
        PORT = re.match(pattern,data).group()
        #如果是则匹配address
        if port == PORT:
            pattern = r'address is (\S+)'
            l = re.findall(pattern,data)
            return l
        else:
            continue

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("argv is error")
    else:
        print(get_address(sys.argv[1]))
