from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DbConnect import DBConnect
from ListRequest import ListTicket

dbconnect=DBConnect()

root=Tk()
root.title("Ticket Reservation")
root.resizable(0,0)
root.configure(background="#e1d8b2")
#style
style=ttk.Style()
style.theme_use('clam')
style.configure('TLabel',background="#e1d8b2")
style.configure('TButton',background="#e1d8b2")
style.configure('TRadiobutton',background="#e1d8b2")
#FullName
ttk.Label(root,text="FullName:").grid(row=0,column=0,padx=10,pady=10)
EntryFullName=ttk.Entry(root,width=30,font=('Impact Regular',16))
EntryFullName.grid(row=0,column=1,columnspan=2,pady=10)
#Gender
ttk.Label(root,text="Gender:").grid(row=1,column=0)
SpanGender=StringVar()
ttk.Radiobutton(root,text="Male",variable=SpanGender,value="Male").grid(row=1,column=1)
ttk.Radiobutton(root,text="Female",variable=SpanGender,value="Female").grid(row=1,column=2)

#Comment
ttk.Label(root,text="Comment:").grid(row=2,column=0)
txtComment=Text(root,width=30,height=15,font=('Arial',16))
txtComment.grid(row=2,column=1,columnspan=2)

#buttons
buSubmit=ttk.Button(root,text="Submit")
buSubmit.grid(row=3,column=3,pady=10)
buList=ttk.Button(root,text="List Res.")
buList.grid(row=3,column=2,pady=10)


def BuSaveData():
    #print("FullName: {}".format(EntryFullName.get()))
    #print("Gender: {}".format(SpanGender.get()))
    #print("Comment: {}".format(txtComment.get(1.0,'end')))
    msg=dbconnect.Add(EntryFullName.get(),SpanGender.get(),txtComment.get(1.0,'end'))
    messagebox.showinfo(title="Add info",message=msg)
    EntryFullName.delete(0,'end')
    txtComment.delete(1.0,'end')

def BuListData():
    #TODO: show orders
    #print(' not implemented yet')
    listrequest=ListTicket()

buSubmit.config(command=BuSaveData)
buList.config(command=BuListData)
root.mainloop()