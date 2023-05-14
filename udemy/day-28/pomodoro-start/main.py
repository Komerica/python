from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# 🟢 Add padding
window.config(padx=100, pady=50, bg=YELLOW)

# 🟥 grid 1
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# 🟥 grid 2 ( include a pic, so use canvas(?) )
# 🟢 Set canvas size
#                                                 highlightthickness = the border line of canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# 🟢 이미지를 이런식으로 받아서 써야함!
tomato_img = PhotoImage(file="tomato.png")

# 🟢 Place tomato_img in the center
canvas.create_image(100, 112, image=tomato_img)

# 🟢 create_image 에 overlap 할 수 있음!
#                  *args == unlimited positional arguments
#                  **kw  == unlimited keyword arguments
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# 🟥 grid 3
start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

# 🟥 grid 4
reset_button = Button(text="reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# 🟥 grid 5
check_marks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20), highlightthickness=0)
check_marks.grid(column=1, row=3)


# canvas.pack()

window.mainloop()
