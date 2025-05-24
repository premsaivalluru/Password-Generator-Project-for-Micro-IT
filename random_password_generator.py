import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    selected_options = []
    if var1.get():
        selected_options.append(string.ascii_uppercase)
    if var2.get():
        selected_options.append(string.ascii_lowercase)
    if var3.get():
        selected_options.append(string.digits)
    if var4.get():
        selected_options.append(string.punctuation)
    try:
        length = int(length_entry.get())
    except:
        messagebox.showwarning("warning","Enter length in digits only!!!")
        return

    if not selected_options:
        messagebox.showwarning("warning","Select atleast one option!!!")
    
    characters = ''.join(selected_options)
    password_string = ''.join(random.choices(characters,k=length))
    password_label.config(text=f"{password_string}")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_label.cget("text"))
    root.update()

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x400")

title_label = tk.Label(root,text="RANDOM PASSWORD GENERATOR",font=("Arial",18),fg='red')
title_label.grid(row=0,column=0,pady=5,padx=10,columnspan=2)

label1 = tk.Label(root,text="Enter password length:")
label1.grid(row=1,column=0,sticky='w',padx=10,pady=5)

length_entry = tk.Entry(root,width=30)
length_entry.grid(row=1,column=1,padx=5,pady=5,sticky='w')

choice_label = tk.Label(root,text="Select inclusive criteria for password:")
choice_label.grid(row=2,column=0,sticky='w',padx=10,pady=5)

var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
var4=tk.IntVar()

uppercase = tk.Checkbutton(root,text="Uppercase Letters",variable=var1)
uppercase.grid(row=3,column=1,sticky='w',padx=10,pady=5)

lowercase = tk.Checkbutton(root,text="Lowercase Letters",variable=var2)
lowercase.grid(row=4,column=1,sticky='w',padx=10,pady=5)

digits = tk.Checkbutton(root,text="Digits",variable=var3)
digits.grid(row=5,column=1,sticky='w',padx=10,pady=5)

special_characters = tk.Checkbutton(root,text="Special Characters",variable=var4)
special_characters.grid(row=6,column=1,sticky='w',padx=10,pady=5)

generate_button = tk.Button(root,text="Generate Password",command=generate_password)
generate_button.grid(row=7,column=1,sticky='w',padx=10,pady=10)

password_label = tk.Label(root,text="",font=("Times New Roman",18))
password_label.grid(row=8,column=0,columnspan=3,padx=10,pady=10)

copy_button = tk.Button(root,text="Copy Password",command=copy_password)
copy_button.grid(row=9,column=0,columnspan=2,pady=10)

root.mainloop()