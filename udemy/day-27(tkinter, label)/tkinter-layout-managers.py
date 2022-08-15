from tkinter import *
###########################
# Tkinter Layout Managers #
###########################
# 1. Pack
#   : It packs each of the widgets next to each other in a vaguely logical format.
#     By default, pack will always start from the top and then pack every other widget just below the previous one.
#     Ex) pack(side="left")  ->  it's going to pack everything starting from the left edge of the program.
# 2. Place
#   : All about precise positioning. Have to provide X, Y value!
# 3. Grid
#   : It imagines taht your entire program is a grid and,
#     you can divide it into any number of columns and rows that you want to.

# 🟥 Error
# cannot use geometry manager pack inside . which already has slaves managed by grid
# -> Never mix grid and pack in the same master window.


def button_clicked():
    print("Button got clicked!")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")    # Change the previous text
# my_label.place(x=0, y=0)    # Another Tkinter Layout Manager out of 3 of them (1.Pack / 2.Place / 3.Grid)
my_label.grid(column=0, row=0)    # Another Tkinter Layout Manager out of 3 of them (1.Pack / 2.Place / 3.Grid)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="New Button!", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()