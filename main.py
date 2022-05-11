import random
import os
import csv
from tkinter import *
from os.path import exists
from turtle import onclick
chck=True
def createpass():
    valchar=['ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz','0123456789',"~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"]
    pss=''
    numcnt=0
    symcnt=0
    for i in range(0,8):
        ind1=random.randint(0,1)
        ind2=random.randint(0,25)
        pss+=valchar[ind1][ind2]
    for i in range(0,5):
        ind1=random.randint(2,3)
        if(ind1==2):
            ind2=random.randint(0,9)
            pss+=valchar[ind1][ind2]
            numcnt+=1
        else:
            ind2=random.randint(0,31)
            pss+=valchar[ind1][ind2]
            symcnt+=1
    if(numcnt==0):
        pss+=valchar[2][random.randint(0,9)]
    elif(symcnt==0):
        pss+=valchar[3][random.randint(0,31)]
    return pss      
def createtext():
    def addtosheet():
        with open('passwords.csv', 'a',encoding='UTF8') as csvfile:
            writer=csv.writer(csvfile)
            pss=passedit.get("1.0","end-1c")
            nam=app_name.get()
            writer.writerow([nam,pss])
            csvfile.close()
        passedit.destroy()
        addto.destroy()
        app_name.delete(0,END)
        sub_name['state']=NORMAL
        warntext.config(text='Last Entry Added')
    txt=app_name.get()
    if(txt==None or txt==''):
        warntext.config(text='Enter an App name!')
        return
    warntext.config(text='Edit Password')
    sub_name['state']=DISABLED
    txt=createpass()
    passedit=Text(win,width=20,height=5)
    passedit.insert(INSERT,txt)
    passedit.grid(row=4,pady=5,columnspan=2)
    addto=Button(win,text='Add to Sheet',command=addtosheet)
    addto.grid(row=5,pady=5,columnspan=2)
print(exists('read.txt'))
file_exists=exists('passwords.csv')
if file_exists==False:
    with open('passwords.csv', 'w',encoding='UTF8') as csvfile:
        row=['Application','Passwords']
        writer = csv.writer(csvfile)
        writer.writerow(row)
        csvfile.close()
win=Tk()
win.title('PassGen Prototype')
win.geometry('400x300')
hel=Label(win,text='Welcome to PassGen v1.0')
hel.grid(columnspan=2,sticky='EW',padx=135)
fil=Label(win,text='Application name:').grid(row=1,column=0,sticky='W',padx=20,pady=10)
app_name=Entry(win)
app_name.grid(row=1,column=1,sticky='W',pady=10)
warntext=Label(win,text='')
sub_name=Button(win,text='Generate',command=createtext)
sub_name.grid(row=2,columnspan=2,padx=135,pady=5)
warntext.grid(row=3,pady=5,padx=135,columnspan=2)
win.mainloop()