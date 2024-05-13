import tkinter
import tkinter.messagebox
import sys

root = tkinter.Tk()
root.title("To-Do List")
root.geometry("400x295")
root.configure(bg="#330099")

button_width = 20
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def exit_app():
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        sys.exit()

frame_tasks = tkinter.Frame(root, bg="light blue")
frame_tasks.place(x=10, y=10)

listbox_tasks = tkinter.Listbox(frame_tasks, height=9, width=60)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root,width=50)
entry_task.place(x=45, y=165,height=25)

button_add_task = tkinter.Button(root, text="Add task", width=button_width, command=add_task)
button_add_task.place(x=120, y=200)

button_delete_task = tkinter.Button(root, text="Delete task", width=button_width, command=delete_task)
button_delete_task.place(x=120, y=230)

button_exit = tkinter.Button(root, text="Exit", width=button_width, command=exit_app)
button_exit.place(x=120, y=260)

root.mainloop()