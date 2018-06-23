# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 09:51:28 2018

@author: hp
"""

from tkinter import *
from tkinter import ttk
import webbrowser

root=Tk()
root.title('Search bar')
#root.iconbitmap('mic.ico')

photo=PhotoImage(file='mic.png').subsample(15,15)

style=ttk.Style()
style.theme_use('winnative')

label1=ttk.Label(root,text='query')
label1.grid(row=0,column=0)
entry1=ttk.Entry(root,width=50)
entry1.grid(row=0,column=1,columnspan=4)

btn2=StringVar()

def callback():
    
    if btn2.get()=='google':
        webbrowser.open('http://google.com/search?q='+entry1.get())
    elif btn2.get()=='duck':
        webbrowser.open('http://duckgo.com/?='+entry1.get())

def get(event):
    
    if btn2.get()=='google':
        webbrowser.open('http://google.com/search?q='+entry1.get())
    elif btn2.get()=='duck':
        webbrowser.open('http://duckgo.com/?='+entry1.get())
        
entry1.bind('<Return>',get)

def buttonClick():
    pass

mybutton1=ttk.Button(root,text='search',width=10,command=callback)
mybutton1.grid(row=0,column=6)

mybutton2=ttk.Radiobutton(root,text='google',value='google',variable=btn2)
mybutton2.grid(row=1,column=1,sticky=W)

mybutton3=ttk.Radiobutton(root,text='flipkart',value='flipkart',variable=btn2)
mybutton3.grid(row=1,column=2,sticky=E)


mybutton4=ttk.Radiobutton(root,text='Youtube',value='Youtube',variable=btn2)
mybutton4.grid(row=1,column=3)


mybutton5=ttk.Radiobutton(root,text='amazon',value='amazon',variable=btn2)
mybutton5.grid(row=1,column=4,sticky=E)

#mybutton6=Button(root,image=photo,command=buttonClick,bd=0,activebackground='#clbfbf',Overrelief='groove',relief='sunken')
#mybutton6.grid(row=0,column=5)                

entry1.focus()
root.wm_attributes('-topmost',1)
root.mainloop()      