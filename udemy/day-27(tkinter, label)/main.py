# TKinter documentation: http://tcl.tk/man/tcl8.6/TkCmd/label.htm
import tkinter

# Tk() is like screen in Turtle!
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# 🟪 Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()     # Pack our label onto the screen! (이 라인이 없으면 label이 안보임!)
                    # pack()안에 들어갈 arguments가 ...면 default value가 있다는 뜻!!
# Packer: Geometry Management System (It's just a simple way to lay out the components that you're building.)

import turtle
tim = turtle.Turtle()
tim.write("Hello")     # arguments중 arg: 에는 ...가 없다. 그러므로 Default 값이 없으므로 무조건 부여해주어야하는 값!

# window.mainloop() behaves like while loop when we covered Turtle
window.mainloop()   # Always at the end of the program
