from tkinter import *
import random
import time
root = Tk()
text = StringVar()
root.title("短信")
root.geometry("600x400+300+200")
label_title = Label(root, text="联系人", font=("黑体", 20))
label_title.place(x=20, y=180)
a=''
s=''
entry = Entry(root, font=("黑体", 20), textvariable=text)
entry.place(x=120, y=70)
texti = StringVar()

def callback7():
    global s
    s = ''
    text.set('') 
    s ='已发送'
    text.set(s)


def callback1():
    global a
    a="小明"
    texti.set(a)

def callback2():
    global a
    a = "小红"
    texti.set(a)

def callback3():
    global a
    a = "小紫"
    texti.set(a)

btn = Button(root, text="小明", font=("黑体", 15), command=callback1)
btn.place(x=30, y=240)
btn = Button(root, text="小红", font=("黑体", 15), command=callback2)
btn.place(x=100, y=290)
btn = Button(root, text="小紫", font=("黑体", 15), command=callback3)
btn.place(x=30, y=340)


entry = Entry(root, font=("黑体", 20), textvariable=texti)
entry.place(x=120, y=180)

btn = Button(root, text="发送", font=("黑体", 15), command=callback7)
btn.place(x=500, y=300)




root.mainloop()
