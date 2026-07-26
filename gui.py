import tkinter as tk
from tkinter import ttk
from cylinder_tab import build_cyl_tab
from motor_tab import build_mot_tab

root = tk.Tk()
root.title("Cylinder Calculator")
root.geometry("500x500")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

build_cyl_tab(notebook)
build_mot_tab(notebook)

root.mainloop()    

