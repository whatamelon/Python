#code10-18.py

from tkinter import *
from tkinter import messagebox

#함수 선언 부분
def func_open() :
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")

def func_exit() :
    window.quit()
    window.destory()

#메인 코드 부분
window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일" , menu = fileMenu)
fileMenu.add_command(label = "열기")
fileMenu.add_separator()
fileMenu.add_command(label = "종료")


window.mainloop()