
import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

# 黄色的显示区域
var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
# 黄色区域 Label控件
l.pack()

# 选取数字并将var1设置为选中的数字
def print_selection():
    # lb.curselection返回当前选定项目的索引
    value = lb.get(lb.curselection())
    var1.set(value)

# 通过按钮的command　可将var1设置为选定的值
b1 = tk.Button(window, text='print selection', width=15,
                height=2, command=print_selection)
# 按钮　Button
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
lb = tk.Listbox(window, listvariable=var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end', item)

lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
# 数字区域　Listbox
lb.pack()

window.mainloop()