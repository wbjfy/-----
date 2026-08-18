import tkinter as tk
from tkinter import filedialog, messagebox

# 创建主窗口
root = tk.Tk()
root.title("简易文本编辑器")
root.geometry("700x500")

# 文本编辑区
text = tk.Text(root, font=("微软雅黑", 11))
text.pack(fill=tk.BOTH, expand=True)

# 功能函数
def new_file():
    text.delete(1.0, tk.END)
    root.title("新建文件 - 文本编辑器")

def open_file():
    path = filedialog.askopenfilename(filetypes=[("文本文件","*.txt"), ("所有文件","*.*")])
    if path:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        text.delete(1.0, tk.END)
        text.insert(1.0, content)
        root.title(path + " - 文本编辑器")

def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("文本文件","*.txt"), ("所有文件","*.*")])
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text.get(1.0, tk.END))
        messagebox.showinfo("提示", "保存成功！")

def clear_text():
    text.delete(1.0, tk.END)

def quit_app():
    root.quit()

# 菜单栏
menu_bar = tk.Menu(root)
# 文件菜单
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="新建", command=new_file)
file_menu.add_command(label="打开", command=open_file)
file_menu.add_command(label="保存", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="清空", command=clear_text)
file_menu.add_command(label="退出", command=quit_app)
menu_bar.add_cascade(label="文件", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()