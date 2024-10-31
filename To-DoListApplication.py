import tkinter as tk
from tkinter import messagebox
import json
import os
from tkinter import *
from tkinter import font

# file to store tasks
file_name = "tasks.json"

# load task from json file
def loadTask():
    if os.path.exists(file_name):
        with open (file_name,"r") as file:
            return json.load(file)
    return []

# Save task to json file
def saveTask(tasks):
    with open (file_name,"w") as file:
        json.dump(tasks,file,indent=4)

# Add a new task
def addTask():
    task_desc = task_entry.get().strip()
    if task_desc :
        tasks.append({"description":task_desc,"status":"pending"})
        updateTaskList()
        saveTask(tasks)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning","Task description cannot be empty.")

# Update the task list display
def updateTaskList():
    task_listbox.delete(0,tk.END)
    for idx,task in enumerate(tasks):
        status = "✓" if task["status"] == "completed" else "✗"
        task_listbox.insert(tk.END, f"{idx + 1}. {task['description']} - {status}")

# Mark selected task as completed
def markTaskCompleted():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["status"] = "completed"
        updateTaskList()
        saveTask(tasks)
    except IndexError:
        messagebox.showwarning("Warning","Please select a task to mark as completed.")

# Delete selected task 
def deleteTask():
    try:
        selected_index = task_listbox.curselection()[0]
        removed_task = tasks.pop(selected_index)
        updateTaskList()
        saveTask(tasks)
        messagebox.showinfo("Info",f"Task '{removed_task['description']} deleted.")
    except IndexError:
        messagebox.showwarning("Warning","Please select a task to delete.")

# Initialize the main Tkinter window

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("800x800")
root.config(bg="#2c3e50")

heading_font = font.Font(family="Helvitica",size=16,weight = "bold")
button_font = font.Font(family="Helvitica",size=12)
entry_font = font.Font(family="Helvitica",size=12)
list_font = font.Font(family="Helvitica",size=12)

heading_label = tk.Label(root,text="To-Do List",font=heading_font,fg="#ecf0f1",bg="#2c3e50")
heading_label.pack(pady=10)

# Task entry
task_entry = tk.Entry(root,width=80,font=entry_font,fg="#2c3e50",highlightbackground="#3498db")
task_entry.pack(pady=20)

# Add task button
add_button = tk.Button(root,text="Add Task",font=button_font,bg="#3498db",fg="white",command=addTask)
add_button.pack(pady=10)

# Task listbox
task_listbox = tk.Listbox(root,width = 80,height=20,font=list_font,bg="#ecf0f1",fg="#2c3e50",selectbackground="#3498db",selectforeground="white") 
task_listbox.pack(pady=20)

# Mark completed and deleted button
completed_button = tk.Button(root,text="Mark as Comleted",font=button_font,bg="#2ecc71",fg="white",command=markTaskCompleted)
completed_button.pack(pady=10)

deleted_button = tk.Button(root,text="Delete Task",font=button_font,bg="#e74c3c",fg="white",command=deleteTask)
deleted_button.pack(pady=10)

# Load initial task and display
tasks = loadTask()
updateTaskList()

# Run the main Tkinter loop
root.mainloop()
