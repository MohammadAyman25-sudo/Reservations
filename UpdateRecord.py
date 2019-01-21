from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DbConnect import DBConnect

dbconnect=DBConnect()

class Updaterecord:
    def __init__(self):
        self._root=Tk()
        self._root.title('Update Record')
        self._root.resizable(0,0)
        self._root.configure(background="#e1d8b2")
        # style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background="#e1d8b2")
        style.configure('TButton', background="#e1d8b2")
        #ID
        lblID = ttk.Label(self._root, text="ID: ",font=('Impact Regular', 12))
        lblID.grid(row=0, column=0, padx=10, pady=10)
        txtID = ttk.Entry(self._root, width=30, font=('Impact Regular', 16))
        txtID.grid(row=0, column=1, columnspan=2, pady=10)
        #Change Comment into
        lblComment = ttk.Label(self._root, text="Change Comment Into: ", font=('Impact Regular', 12))
        lblComment.grid(row=1, column=0, padx=10, pady=10)
        txtComment = Text(self._root, width=30,height=15, font=('Impact Regular', 16))
        txtComment.grid(row=1, column=1, columnspan=2, pady=10)
        btnUpdate=ttk.Button(self._root,text='Update Record',width=30)
        btnUpdate.grid(row=2, column=2, padx=10, pady=10)

        def BuUpdate():
            msg=dbconnect.UpdateRecord(txtID.get(),txtComment.get(1.0,'end'))
            messagebox.showinfo(title='Update info',message=msg)
            txtID.delete(0,'end')
            txtComment.delete(1.0,'end')
        btnUpdate.config(command=BuUpdate)
        self._root.mainloop()
#Updaterecord()