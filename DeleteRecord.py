from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DbConnect import DBConnect

dbconnect=DBConnect()

class Deleterecord:
    def __init__(self):

        self._root=Tk()
        self._root.title('Delete Record')
        self._root.resizable(0, 0)
        self._root.configure(background="#e1d8b2")
        # style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background="#e1d8b2")
        style.configure('TButton', background="#e1d8b2")

        lblID=ttk.Label(self._root,text="ID: ")
        lblID.grid(row=0, column=0,padx=10,pady=10)
        txtID=ttk.Entry(self._root,width=30,font=('Impact Regular',16))
        txtID.grid(row=0,column=1,columnspan=2,pady=10)
        btndelete=ttk.Button(self._root,text="Delete Record",width=30)
        btndelete.grid(row=1,column=0,pady=10)


        def BuDelete():
            msg=dbconnect.DeleteRecord(txtID.get())
            messagebox.showinfo(title="Delete info", message=msg)
            txtID.delete(0,'end')

        btndelete.config(command=BuDelete)
        self._root.mainloop()
#Deleterecord()