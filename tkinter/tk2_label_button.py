
import tkinter as tk

window = tk.Tk()
window.title('我的窗口')
# 设置窗口大小
window.geometry('200x100')

#　用来跟踪变量值的变化,初始化为空
var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green',
    font=("Arial", 12), width=15, height=2)
# 必须要有，否则不会显示
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

b = tk.Button(window, text='hit me', width=15,
    height=2, command=hit_me)
b.pack()

window.mainloop()
