from tkinter import *
from tkinter.messagebox import showinfo
import tkinter.ttk as ttk
import time

# 참고: https://www.pythontutorial.net/tkinter/tkinter-progressbar/

#####################
# Progress bar 연습 #
#####################

root = Tk()
root.title("Nado GUI")
root.geometry("300x150")
root.config(bg="gray")


def start_progress():
    for i in range(1, 101):
        time.sleep(0.03)
        p_var3.set(i)
        progressbar3.update()
        progress_label['text'] = update_progress_label()
    if progressbar3['value'] == 100:
        showinfo(message="The progress completed!")


def stop_progress():
    progressbar3.stop()
    progress_label['text'] = update_progress_label()


def update_progress_label():
    return f"Current Progress: {progressbar3['value']}%"


p_var3 = IntVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=280, variable=p_var3)
progressbar3.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

progress_label = Label(root, text=f"Current Progress: {progressbar3['value']}%")
progress_label.grid(column=0, row=1, columnspan=2)

start_btn = Button(root, text="Start", command=start_progress)
start_btn.grid(column=0, row=2, padx=10, pady=10, sticky=E)

stop_btn = Button(root, text="Stop", command=stop_progress)
stop_btn.grid(column=1, row=2, padx=10, pady=10, sticky=W)

root.mainloop()