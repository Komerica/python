from tkinter import *

window = Tk()   # Creating a window
window.title("My First GUI Program")
window.minsize(width=500, height=300)

###############
### Widgets ###
###############

# 🟪 Label
# TKinter Label documentation: http://tcl.tk/man/tcl8.6/TkCmd/label.htm
my_label = Label(text="I Am a Label")   # Creating a label
my_label.pack()     # Putting the label on the window

# 🧡 How to change Label
# 방법1)
# my_label["text"] = "New Label"
# 방법2)
my_label.config(text="New Label")


# 🟪 Button
def button_clicked():
    print("I got clicked")


def change_text():
    user_input = input.get()
    my_label.config(text=user_input)


button = Button(text="Click me!", command=change_text)
button.pack()


# 🟪 Entry: Text box (User Input)
# TKinter Entry documentation: http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
input = Entry(width=10)
input.pack()


# 🟪 Text Entry box: Multiple lines of text
# Ex1)
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")    # Add some text to begin with
print(entry.get())
entry.pack()

# Ex2)
text = Text(height=5, width=30)
text.focus()    # Puts cursor in textbox
text.insert(END, "Example of multi-line text entry.")   # Add some text to begin with
print(text.get("1.0", END))     # Gets current value in textbox at line 1, character 0
text.pack()


# 🟪 Spin box: Counter
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# 🟪 Scale: Slider
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# 🟪 Check Box: On or Off (Tick box)
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# Variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()    # ↓ This will keep track of the value of the checkbox ↓
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# 🟪 Radio Buttons:
def radio_used():
    # The value of each of the radio buttons will get printed!
    print(radio_state.get())    # value=1 for radiobutton1  /   value=2 for radiobutton2


radio_state = IntVar()  # Variable to hold on to which radio button value is checked.
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# 🟪 List box of choices:
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()   # Opening the window

