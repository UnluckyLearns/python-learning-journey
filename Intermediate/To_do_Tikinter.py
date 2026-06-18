import tkinter as tk
import os
import json

class ToDo():
    def __init__(self,name,complete):
        self.name = name
        self.complete = complete


class ToDoManager():
    def __init__(self):
        self.entries = {}
        self.entries["Tasks"] = []

    def add_task(self,name):
        entry = ToDo(name,False)
        self.entries["Tasks"].append({"Task" : entry.name ,"Completed" : entry.complete})

    def load_tasks(self):
        if os.path.isfile(r"PATH"):
            with open(r"PATH","r") as file:
                self.entries = json.load(file)

    def save_tasks(self):
        with open(r"PATH","w") as file:
            json.dump(self.entries,file,indent=2)

    def complete(self,value):
        for items in self.entries["Tasks"]:
            if items["Task"] == value:
                items["Completed"] =  not items["Completed"]
                print(items["Completed"])
    def delete(self,cook):
        del self.entries["Tasks"][int(cook)]
        


def main():
    manager = ToDoManager()
    manager.load_tasks()
    
    def display():
        task_list.delete(0, tk.END)
        for items in manager.entries["Tasks"]:
            if items["Completed"] == False:
                task_list.insert(tk.END,items["Task"] + "------x")
            else:
                task_list.insert(tk.END,items["Task"] + "------✓")
                
    def add_to_list(event=None):
        name = text.get()
        if name:
            manager.add_task(name)
            display() 
            text.delete(0,tk.END)
            manager.save_tasks()

    def complete_task(event=None):
        cook = task_list.curselection()
        if not cook:
             return
        value = task_list.get(cook[0])
        manager.complete(value.split("------")[0])
        manager.save_tasks()
        display()

    def delete_task(event=None):
        cook = task_list.curselection()
        if not cook:
            return
        manager.delete(cook[0])
        manager.save_tasks()
        display()

    root = tk.Tk()
    root.title("TO DO APP")
    root.columnconfigure(0,weight = 1)
    root.rowconfigure(0,weight= 1)


    frame = tk.Frame(root)
    frame.grid(row=0,column=0,sticky="nsew")
    frame.columnconfigure(0,weight = 1)
    frame.rowconfigure(0,weight= 1)
    text = tk.Entry(frame)
    text.grid(row=0,column=0)
    text.bind("<Return>",add_to_list)
    but = tk.Button(frame,text="Add Task", command=add_to_list)
    but.grid(row=0,column=1)



    frame_label = tk.LabelFrame(root,text="TASKS : ")
    frame_label.grid(row=1,column=0,sticky="nsew")
    frame_label.columnconfigure(0,weight = 1) 
    frame_label.rowconfigure(0,weight= 1)
    task_list = tk.Listbox(frame_label)
    task_list.grid(row=1,column=0,columnspan=2,sticky="ew")
    display()

    frame2 = tk.Frame(root)
    frame2.grid(row=2,column=0,sticky="ew")
    frame2.columnconfigure(0,weight = 1)
    frame2.rowconfigure(0,weight= 1)
    but2 = tk.Button(frame2,text="Delet Task ",command=delete_task)
    but2.grid(row=0,column=0,sticky="ew")
    but3 = tk.Button(frame2,text="Complete Task",command=complete_task)
    but3.grid(row=0,column=1,sticky="ew")
    but4 = tk.Button(frame2,text="Save To Json File",command=manager.save_tasks)
    but4.grid(row=0,column=2,sticky="ew")

    root.mainloop()
if __name__ == "__main__":
    main()