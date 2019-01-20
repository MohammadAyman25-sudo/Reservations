from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DbConnect import DBConnect

dbconnect=DBConnect()

class Deleterecord:
    def __init__(self):

        self._root=Tk()
        self._root.title('Delete Record')

        lblID=ttk.Label(self._root,text="ID: ")
        lblID.grid(row=0, column=0,padx=10,pady=10)
        txtID=ttk.Entry(self._root,width=30,font=('Impact Regular',16))
        txtID.grid(row=0,column=1,columnspan=2,pady=10)
        btndelete=ttk.Button(self._root,text="Delete Record",width=30)
        btndelete.grid(row=1,column=0,pady=10)


        def BuDelete():
            msg=dbconnect.DeleteRecord(txtID.get())
            messagebox.showinfo(title="Delete info", message=msg)

        btndelete.config(command=BuDelete)
        self._root.mainloop()
#deleterecord()