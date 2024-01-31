from tkinter import*
import sys
root = Tk()
root.geometry('470x320')
root.resizable(0,0)
root.title('contact')
root.config(bg = '#0808d8')
#=========def===========

def insert():
    name = ent_fname.get()
    lname = ent_lname.get()
    city = ent_city.get()
    tel = ent_tel.get()
    lstbox.insert(END,f'{name},{lname},{city},{tel}')
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_city.delete(0,END)
    ent_tel.delete(0,END)
    ent_fname.focus_set()
def delete():
    n = lstbox.curselection()
    lstbox.delete(n)
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_city.delete(0,END)
    ent_tel.delete(0,END)
def fetch():
    clear()
    n = lstbox.curselection()
    data = lstbox.get(n)
    lst = data.split(',')
    ent_fname.insert(0,lst[0])
    ent_lname.insert(0,lst[1])
    ent_city.insert(0,lst[2])
    ent_tel.insert(0,lst[3])
    lstbox.delete(n)

def exit():
    sys.exit(0)



#=========label==========
label_fname = Label(root,text='fneme: ', font= ('IranNastaliq 12') , bg = '#0808d8' , fg= '#f7f725')
label_fname.place(x=20,y=10)

label_city = Label(root,text='city: ', font= ('IranNastaliq 12') , bg = '#0808d8' , fg= '#f7f725')
label_city.place(x=20,y=50)

label_lname = Label(root,text='lname: ', font= ('IranNastaliq 12') , bg = '#0808d8' , fg= '#f7f725')
label_lname.place(x=240,y=10)

lable_tel = Label(root,text='tel: ', font= ('IranNastaliq 12') , bg = '#0808d8' , fg= '#f7f725')
lable_tel.place(x=240,y=50)

#=============entry============
ent_fname = Entry(root , )
ent_fname.place(x=100,y=20)

ent_city = Entry(root , )
ent_city.place(x=100,y=60)

ent_lname = Entry(root , )
ent_lname.place(x=320,y=20)

ent_tel = Entry(root , )
ent_tel.place(x=320,y=60)

#============botton===========
btn_insert = Button(root, text= 'insert' , font=('Algerian 15'),fg= '#0808d8' ,bg='#f7f725', command=insert)
btn_insert.place(x=360, y=100)

btn_Delete = Button(root, text= 'Delete' , font=('Algerian 14') ,fg= '#0808d8' ,bg='#f7f725', command=delete)
btn_Delete.place(x=360, y=140)

btn_clear = Button(root, text= 'clear' , font=('Algerian 15') ,fg= '#0808d8' ,bg='#f7f725', command=clear)
btn_clear.place(x=360, y=180)

btn_fetch = Button(root, text= 'fetch' , font=('Algerian 15') ,fg= '#0808d8' ,bg='#f7f725', command= fetch)
btn_fetch.place(x=360, y=220)

btn_Exit = Button(root, text= 'Exit' , font=('Algerian 15') ,fg= '#0808d8' ,bg='#f7f725', command=exit)
btn_Exit.place(x=360, y=260)


lstbox = Listbox(root, width=55 , height= 12 , fg = '#0808d8')
lstbox.place(x=20 , y=100)





root.mainloop()