from tkinter import *
import time
root = Tk()
root.title('手机')
root.geometry('375x667+700+300')
s=''
j = 0
label_title = Label(root, text='请输入密码：', font=('黑体', 20))
label_title.place(x=80,y=10)
text = StringVar()
label_title = Label(root, text='', font=('黑体', 20), textvariable=text)
label_title.place(x=130, y=40)
def callback1():
    global s
    s = s + '1'
    text.set(s)
def callback2():
    global s
    s = s + '2'
    text.set(s)
def callback3():
    global s
    s = s + '3'
    text.set(s)
def callback4():
    global s
    s = s + '4'
    text.set(s)
def callback5():
    global s
    s = s + '5'
    text.set(s)
def callback6():
    global s
    s = s + '6'
    text.set(s)
def callback7():
    global s
    s = s + '7'
    text.set(s)
def callback8():
    global s
    s = s + '8'
    text.set(s)
def callback9():
    global s
    s = s + '9'
    text.set(s)
def callback11():
    global s
    s = s + '0'
    text.set(s)
def a():
    global s

    s = s[0:-1]
    text.set(s)
def b():
    global s
    global j
    while True:
        if s == '8796':
            text.set('密码正确')
            
            break
        else:
            text.set('密码错误')
            s = ''
            
            root.mainloop()
btn = Button(root, text=' 1 ', font=('黑体', 25), command=callback1)
btn.place(x=30, y=120)
btn = Button(root, text=' 2 ', font=('黑体', 25), command=callback2)
btn.place(x=150, y=120)
btn = Button(root, text=' 3 ', font=('黑体', 25), command=callback3)
btn.place(x=270, y=120)
btn = Button(root, text=' 4 ', font=('黑体', 25), command=callback4)
btn.place(x=30, y=220)
btn = Button(root, text=' 5 ', font=('黑体', 25), command=callback5)
btn.place(x=150, y=220)
btn = Button(root, text=' 6 ', font=('黑体', 25), command=callback6)
btn.place(x=270, y=220)
btn = Button(root, text=' 7 ', font=('黑体', 25), command=callback7)
btn.place(x=30, y=320)
btn = Button(root, text=' 8 ', font=('黑体', 25), command=callback8)
btn.place(x=150, y=320)
btn = Button(root, text=' 9 ', font=('黑体', 25), command=callback9)
btn.place(x=270, y=320)
btn = Button(root, text=' ← ', font=('黑体', 25), command=a)
btn.place(x=30, y=420)
btn = Button(root, text=' 0 ', font=('黑体', 25), command=callback11)
btn.place(x=150, y=420)
btn = Button(root, text=' ✔ ', font=('黑体', 25),command=b)
btn.place(x=270, y=420)
root.mainloop()
