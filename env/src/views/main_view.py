"""
def get_ships_details():
    file_path ="C:\\Users\\venti\\Downloads\\AIS_2021_01_01\\AIS_2021_01_01.csv"
    data_management.insert_data_from_csv_to_mongodb(file_path)
"""

import tkinter as tk
from tkinter import filedialog
from ttkbootstrap.constants import *
import ttkbootstrap as tkboot

files = [(1, "AIS01_01_22", "2024-05-15"), (2, "AIS02_01_22", "2024-05-14"), (3, "AIS03_01_22", "2024-05-13")]

def browse_files():
    filename = filedialog.askopenfilename(initialdir="/Desktop", title="Select a File", filetypes=(("Text files", "*.txt*"), ("All files", "*.*")))
    if filename:
        entry.delete(0, tk.END)
        entry.insert(0,filename)
        
        
def import_file():
    filepath = entry.get()
    #Add logic
    print("Importing file: ", filepath)

def choose_file():
    selected_index = list_box.curselection()
    if selected_index:
        file_id = files[selected_index[0]][0]
        handle_record_action(file_id)
        print(file_id)
    
def handle_record_action(record_id):
    print("Action for record ID:", record_id)
    
        
#Root
root = tkboot.Window(themename="darkly")
root.geometry('500x400')

#File Frame
#--------------------------------------------------------
#Import File
file_frame = tkboot.LabelFrame(root, text="Files")
file_frame.grid(row=0, column=0, padx=20, pady=15, sticky="nsew")

entry = tkboot.Entry(file_frame)
entry.pack(side="top", padx=10, pady=5)       

browse_button = tkboot.Button(file_frame, text="Browse", command=browse_files)
browse_button.pack(side="top", padx=4, pady=10)

import_button = tkboot.Button(file_frame, text="Import", command=import_file)
import_button.pack(side="top", padx=8, pady=4)

#Display list of files
list_box = tk.Listbox(file_frame)
list_box.pack(side="top", padx=20, pady=10)

for file in files:
    list_box.insert(tk.END, f"{file[1]} - {file[2]}")

button = tkboot.Button(file_frame, text="Action", command=choose_file)
button.pack(side="bottom", padx=5)

#Ship Frame
#-------------------------------------------------------------
ship_frame = tkboot.LabelFrame(root, text="Ship Details")
ship_frame.grid(row=0, column=3, padx=20, pady=15, sticky="nsew")

list_ship_box = tk.Listbox(ship_frame)
list_ship_box.pack(side="top", padx=20, pady=10)
root.mainloop()