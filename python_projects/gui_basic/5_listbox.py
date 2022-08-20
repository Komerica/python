from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# selectmode="single" : 한 가지만 선택가능
# selectmode="extended" : 여러 가지 메뉴 선택가능
# height=0 : 리스트 모든 목록이 보인다.
# height=3 : 리스트 3가지 목록만 보인다.
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")   # 0 index 이후에 추가하는 것들은 전부다 END로 해줘도 됨!(끝에다가 추가)
listbox.insert(END, "포도")   # 0 index 이후에 추가하는 것들은 전부다 END로 해줘도 됨!(끝에다가 추가)
listbox.pack()


def btncmd():
    # 삭제
    # listbox.delete(0)  # 맨 앞 항목 삭제
    # listbox.delete(END)  # 맨 뒤 항목 삭제

    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인
    print("1번째부터 3번째까지의 항목: ", listbox.get(0, 2))   # get(): tuple로 뽑힘

    # 선택된 항목 확인 (return index)
    print("선택된 항목: ", listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
