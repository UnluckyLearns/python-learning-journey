import tkinter as tk
from tkinter import ttk
import json
import os

class Notes:
    def __init__(self):
        self.entries = {}
        self.entries["Notes"] = []
    def add_entry(self,title,notes):
        temp_dict = {}
        temp_dict[title]= notes
        self.entries["Notes"].append(temp_dict)

    def save_entry(self):
        with open(r"PATH","w") as file:
            json.dump(self.entries,file,indent=2)
    
    def load_entry(self):
        if os.path.isfile(r"PATH"):
            with open(r"PATH","r") as file:
                self.entries = json.load(file)
    
    def delete_entry(self,index):
        del self.entries["Notes"][index]
    
    def update_entry(self,index,title,notes):
        self.entries["Notes"][index][title] = notes


def main():
    manager = Notes()
    manager.load_entry()
    def added(event=None):
        if txt1 and ent1:
            title = ent1.get()
            notes = txt1.get("1.0", tk.END).splitlines()
            manager.add_entry(title,notes)
        manager.save_entry()
  
    def get_options(event=None):
        options = []
        for items in manager.entries["Notes"]:
            options.append(next(iter(items)))
        ent2['values'] = options
        return options
    
    def get_display(event=None):
        lis1.delete(0,tk.END)
        for items in manager.entries["Notes"]:
            if ent2['values'][ent2.current()] in items:
                for str in items[ent2['values'][ent2.current()]]:
                    lis1.insert(tk.END,str)
    
    def delete(event=None):
        manager.delete_entry(ent2.current())
        get_options()
        ent2.set("Select an option")
        manager.save_entry()
    
    def edit(even=None):
        notes = txt1.get("1.0", tk.END).splitlines()
        manager.update_entry(ent2.current(),ent2.get(),notes)
        manager.save_entry()


    root = tk.Tk()
    root.title('Notes')
    root.geometry("500x500")


    frame = tk.LabelFrame(root,text="Input",background='green')
    frame.pack(fill="x")
    frame.columnconfigure(0,weight = 1)
    frame.columnconfigure(1,weight = 1)
    frame.columnconfigure(2,weight = 1)
    frame.rowconfigure(0,weight = 1)
    frame.rowconfigure(1,weight = 1)

    lab1 = ttk.Label(frame,text = "Title : ",background="green")
    lab1.grid(column=0,row=0)
    ent1 = tk.Entry(frame)
    ent1.grid(column=1,row=0)
    lab2 = ttk.Label(frame,text = "Search : ",background="green")
    lab2.grid(column=0,row=1)
    ent2 = ttk.Combobox(frame,state='readonly')
    ent2.set("Select an option")
    ent2.grid(column=1,row=1)
    but = tk.Button(frame,text="Show",command=get_display)
    but.grid(row=0,column=2,rowspan=2)

    frame3 = tk.LabelFrame(root,text="Content : ",background='red')
    txt1 = tk.Text(frame3, height=10)
    txt1.pack(side="left",fill="x",expand=True)
    frame3.pack(fill="x")
    
    
    frame2 = tk.LabelFrame(root,text="Note List",background='blue')
    lis1 = tk.Listbox(frame2,background="black",foreground="white")
    lis1.pack(side="left",fill="x",expand=True)
    frame2.pack(fill="x")

    frame4 = tk.LabelFrame(root,text="Update Or Create Notes : ",background='yellow')
    frame4.pack(fill="both",expand=True)
    frame4.columnconfigure(0,weight = 1)
    frame4.columnconfigure(1,weight = 1)
    frame4.columnconfigure(2,weight = 1)
    frame4.columnconfigure(3,weight = 1)
    frame4.rowconfigure(1,weight = 1)
    frame4.rowconfigure(0,weight = 1)
    but1 = tk.Button(frame4,text="Add",command=added)
    but1.grid(row=0,column=0,rowspan=2)
    but2 = tk.Button(frame4,text="Update",command=get_options)
    but2.grid(row=0,column=1,rowspan=2)
    but3 = tk.Button(frame4,text="Delete",command=delete)
    but3.grid(row=0,column=2,rowspan=2)
    but4 = tk.Button(frame4,text="Edit",command=edit)
    but4.grid(row=0,column=3,rowspan=2)
    


    root.after_idle(get_options)
    root.mainloop()


if __name__=="__main__":
    main()