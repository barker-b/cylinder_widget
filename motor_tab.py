from tkinter import ttk
import calculator as calc

def build_mot_tab(notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Motor")

    frame = ttk.Frame(tab)
    frame.pack(side="left", anchor="n", padx=20, pady=20)
