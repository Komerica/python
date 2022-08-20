from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 🟪 Text: 여러줄
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

# 🟪 Entry: 한줄     Ex) ID, Password
e = Entry(root, width=30)
e.pack()
# 현재는 값이 비어 있으므로 END를 써도 0과 동일!
# e.insert(END, "한 줄만 입력해요")
e.insert(0, "한 줄만 입력해요")

# 🟪 Print whatever is written in Entry / Text
def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 1: 첫번째 라인  /  0: 0번째 column  /  END: 끝까지
    print(e.get())
    
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()