from tkinter import *
from tkinter import ttk
from DbConnect import DBConnect
from DeleteRecord import Deleterecord
from UpdateRecord import Updaterecord

dbconnect=DBConnect()

class ListTicket:

    def __init__(self):
        self._root=Tk()
        self._root.title('List Request')
        self._root.resizable(0, 0)
        self._root.configure(background="#e1d8b2")

        #Tree View
        self._frame=ttk.Frame(self._root,width=300,height=100)
        self._frame.grid(row=0,column=0,columnspan=3)
        self._dbconnect=DBConnect()
        tv=ttk.Treeview(self._frame)
        tv.pack()
        tv.heading('#0',text='ID')
        tv.configure(column=('#Name','#Gender','#Comment'))
        tv.heading('#Name', text='Name')
        tv.heading('#Gender', text='Gender')
        tv.heading('#Comment', text='Comment')

        buDelete = ttk.Button(self._root, text="Delete Record" )
        buDelete.grid(row=0, column=3, pady=10)

        buUpdate = ttk.Button(self._root, text="Update Record")
        buUpdate.grid(row=1, column=3, pady=10)
        # style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background="#e1d8b2")
        style.configure('TButton', background="#e1d8b2")
        cursor=self._dbconnect.ListRequest()

        for row in cursor:
            tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
            tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
            tv.set('#{}'.format(row['ID']), '#Gender', row['Gender'])
            tv.set('#{}'.format(row['ID']), '#Comment', row['Comment'])

        def BuDelete():
            #print('Hello Delete')
            deleterecord=Deleterecord()
            #msg=dbconnect.DeleteRecord(DeleteRecord.BuDelete())
            #messagebox.showinfo(title="Delete info", message=msg)

        def BuUpdate():
            #print("hello update")
            updaterecord=Updaterecord()
            #msg = dbconnect.UpdateRecord(row['ID'], row['Comment'])
            #messagebox.showinfo(title="Update info", message=msg)

        buDelete.config(command=BuDelete)
        buUpdate.config(command=BuUpdate)


        self._root.mainloop()


#ListTicket()


