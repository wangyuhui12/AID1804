
import random,math
from tkinter import *
from tkinter import messagebox

class map2048():
    def reset(self):
        self.data = [[0 for x in range(4)]
                     for y in range(4)]
        self.fill2()
        self.fill2()

    def __init__(self):
        self.reset()

    def transpose(self):
        return [list(row) for row in zip(*self.data)]

    def invert(self):
        return [row[::-1] for row in self.data]

    def get_space_count(self):
        count = 0
        for row in self.data:
            count += row.count(0)
        return count

    def get_score(self):
        score = 0
        for row in self.data:
            for c in row:
                score += 0 if c < 4 else c * int(math.log(c, 2) - 1)
        return score

    def fill2(self):
        blank_count = self.get_space_count()
        if blank_count == 0:
            return False
        pos = random.randrange(0, blank_count)
        offset = 0
        for row in self.data:
            for i in range(3):
                if row[i] == 0: # 必须加否则覆盖已有的数据
                    if offset == pos:
                        row[i] = 4 if random.randrange(100) > 89 else 2
                        return True
                    offset += 1

    def is_gameover(self):
        for row in self.data:
            if row.count(0):
                return False
            for i in range(3):
                if row[i] == row[i+1]:
                    return False

        self.data = self.transpose()
        for r in self.data:
            for i in range(3):
                if r[i] == r[i+1]:
                    return False
        self.data = self.transpose()
        return True

    def left(self):
        moveflag = False
        def change_row(data):
            new_data = []
            for row in data:
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                new_data.append(new_row)
            return new_data

        for r in self.data:
            for i in range(3):
                if r[i] == 0:
                    moveflag = True

        if moveflag:
            self.data = change_row(self.data)

        for r in self.data:
            for i in range(3):
                if r[i] == r[i+1]:
                    moveflag = True
                    r[i] *= 2
                    r[i+1] = 0
        self.data = change_row(self.data)
        return moveflag

    def right(self):
        self.data = self.invert()
        moveflag = self.left()
        self.data = self.invert()
        return moveflag

    def up(self):
        self.data = self.transpose()
        moveflag = self.left()
        self.data = self.transpose()
        return moveflag

    def down(self):
        self.data.reverse()
        moveflag = self.up()
        self.data.reverse()
        return moveflag

game = map2048()
keymap = {
    'a': game.left,
    'd': game.right,
    'w': game.up,
    's': game.down,
    'Left': game.left,
    'Right': game.right,
    'Up': game.up,
    'Down': game.down,
    'q': exit,
}

game_bg_color = "#bbada0"
mapcolor = {
    0: ("#cdc1b4", "#776e65"),
    2: ("#eee4da", "#776e65"),
    4: ("#ede0c8", "#f9f6f2"),
    8: ("#f2b179", "#f9f6f2"),
    16: ("#f59563", "#f9f6f2"),
    32: ("#f67c5f", "#f9f6f2"),
    64: ("#f65e3b", "#f9f6f2"),
    128: ("#edcf72", "#f9f6f2"),
    256: ("#edcc61", "#f9f6f2"),
    512: ("#e4c02a", "#f9f6f2"),
    1024: ("#e2ba13", "#f9f6f2"),
    2048: ("#ecc400", "#f9f6f2"),
    4096: ("#ae84a8", "#f9f6f2"),
    8192: ("#b06ca8", "#f9f6f2"),
}

map_labels = []
def on_mouse_down(event):
    print("clicked at", event.x, event.y)

def on_key_down(event):
    keysym = event.keysym
    if keysym in keymap:
        if keymap[keysym]():
            game.fill2()
    update_ui()
    if game.is_gameover():
        mb = messagebox.askyesno(title="gameover", message="游戏结束!\n是否退出游戏!")
        if mb:
            exit()
        else:
            game.reset()
            update_ui()

def update_ui():
    for r in range(len(game.data)):
        for c in range(len(game.data[0])):
            number = game.data[r][c]
            label = map_labels[r][c]
            label['text'] = str(number) if number else ''
            label['bg'] = mapcolor[number][0]
            label['foreground'] = mapcolor[number][1]
    label_score['text'] = str(game.get_score())

# 以下为2048的界面
root = Tk()
root.title('2048')
frame = Frame(root, width=300, height=300, bg=game_bg_color)
frame.grid(sticky=N+E+W+S)
frame.focus_set()
frame.bind("<Key>", on_key_down)
frame.bind("<ButtonRelease-1>", on_mouse_down)

# 初始化图形界面
for r in range(len(game.data)):
    row = []
    for c in range(len(game.data[0])):
        value = game.data[r][c]
        text = '' if 0 == value else str(value)
        label = Label(frame, text=text, width=4, height=2,
                      font=("黑体", 30, "bold"))
        label.grid(row=r, column=c, padx=5, pady=5, sticky=N+E+W+S)
        row.append(label)
    map_labels.append(row)
bottom_row = len(game.data)
print("button", str(bottom_row))
label = Label(frame, text='分数', font=("黑体", 30, "bold"),
              bg="#bbada0", fg="#eee4da")
label.grid(row=bottom_row, column=0, padx=5, pady=5)
label_score = Label(frame, text='0', font=("黑体", 30, "bold"),
                    bg="#bbada0", fg="#ffffff")
label_score.grid(row=bottom_row, columnspan=2, column=1, padx=5, pady=5)

def reset_game():
    game.reset()
    update_ui()

restart_button = Button(frame, text='重新开始', font=("黑体", 16, "bold"),
                        bg="#8f7a66", fg="#f9f6f2", command=reset_game)
restart_button.grid(row=bottom_row, column=3, padx=5, pady=5)
update_ui()
root.mainloop()
