import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")  # indeterminate: 쉽게 가늠할 수 없는
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")    # determinate: 확정적인, 확실한
# progressbar.start(10)   # 10ms 마다 움직임
# progressbar.pack()
#
# def btncmd():
#     progressbar.stop()
#
#
# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01)    # 0.01초 대기

        p_var2.set(i)       # progress bar의 값을 설정
        progressbar2.update()   # UI 업데이트
        print(p_var2.get())


btn = Button(root, text="시작", command=btncmd2)
btn.pack()



root.mainloop()
