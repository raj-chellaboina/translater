#required modules
import googletrans
from tkinter import *
from tkinter import ttk,messagebox
from googletrans import Translator,LANGUAGES


#main_alogorithm
root=Tk()
root.title("Transulter")
root.geometry("1080x400")


#Label_Change_function

def Label_Change():
    c1=combo1.get()
    c2=combo2.get()
    label1.config(text=c1)
    label2.config(text=c2)
    root.after(1000,Label_Change)


#Transulate_function

def Transulate_fun():
    try:
        traslator=Translator()
        traslated=traslator.translate(text=text1.get(1.0,END),src=combo1.get(),dest=combo2.get())
        text2.delete(1.0,END)
        text2.insert(END,traslated.text)
    except Exception as e:
        messagebox.showerror("Transulater","Try Agin!")


#arrow
#arrow_image=PhotoImage(file="arrow.png")
#image_label=Label(root,image=arrow_image,width=150)
#image_label.place(x=460,y=50)

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

#Left side

combo1=ttk.Combobox(root,values=languageV,font="Roboto 14" ,state="r")
combo1.place(x=110,y=20)
combo1.set("english")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

frame1=Frame(root,bg="Black",bd=5)
frame1.place(x=10,y=118,width=440,height=210)

text1=Text(frame1,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(frame1)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#right side

combo2=ttk.Combobox(root,values=languageV,font="Roboto 14" ,state="r")
combo2.place(x=730,y=20)
combo2.set("Select Language")

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

frame2=Frame(root,bg="Black",bd=5)
frame2.place(x=620,y=118,width=440,height=210)

text2=Text(frame2,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(frame2)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


#TransulateButon

transulate_button=Button(root,text="Transulate",font="Roboto 15 bold italic",
                         activebackground="white",cursor="hand2",bd=5,
                         bg="red",fg="white",command=Transulate_fun)
transulate_button.place(x=480,y=250)


Label_Change()
root.mainloop()

