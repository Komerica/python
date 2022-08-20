from tkinter import *

# Label: 글자 / 이미지를 보여줌

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="img.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또 만나요")
    # Garbage collection: 불필요한 메모리 공간 해제 (돌아다니면서 쓰레기를 줍는 녀석!)
    #                     photo2 를 전역변수로 설정해주지 않으면 얘는 쓰레기구나 하고 Garbage collection이라는 친구가 쓰레기로 취급해버림!
    global photo2
    photo2 = PhotoImage(file="img2.png")
    label2.config(image=photo2)


btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()