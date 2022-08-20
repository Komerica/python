from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")
# root.geometry("640x480+100+300")    # 가로 x 세로 + x좌표 + y좌표 (컴퓨터 화면 기준 (100,300))
root.resizable(False, False)    # x(너비), y(높이) 값 변경 불가!(창 크기 변경 X)

root.mainloop()