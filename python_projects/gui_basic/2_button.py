from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")     # root(main window;메인 창)에다가 Button을 삽입!
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")    # padx / pady: Button 내의 padding을 준다!
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼33333333333")    # padx / pady: Button 내의 padding을 준다!
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4444444444")    # 글자가 잘릴 지언정 버튼의 너비/높이는 같게 유지!
btn4.pack()

btn5 = Button(root, fg="red", bg="black", text="버튼5")    # fg = foreground
btn5.pack()

photo = PhotoImage(file="img.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼이 클릭되었어요")


btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()