from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("Nado GUI")
root.config(bg="black")


def create_new_file():
    print("Created New File!")


menu = Menu(root)

# File
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New Project", command=create_new_file)
menu_file.add_command(label="New")
menu_file.add_command(label="New Scratch File")
menu_file.add_command(label="Save As...", state="disabled")
menu_file.add_separator()
menu.add_cascade(label="File", menu=menu_file)

# Edit
menu_edit = Menu(menu, tearoff=0)   # 생략 가능
menu.add_cascade(label="Edit", menu=menu_edit)

# Language
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="C++")
menu_lang.add_radiobutton(label="Java")
menu.add_cascade(label="Language", menu=menu_lang)

# View
view_menu = Menu(menu, tearoff=0)
view_menu.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=view_menu)

root.config(menu=menu)
root.mainloop()
