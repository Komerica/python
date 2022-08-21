from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")
root.config(bg="black") # background color: black

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

# 1.File Menu
# 위에 생선된 menu 변수에다가 집어 넣는다! -> Menu(menu, )
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disabled")   # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# 2.Edit Menu (빈값)
menu.add_cascade(label="Edit")

# 3.Language Menu 추가 (radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# 4.View Menu
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()
