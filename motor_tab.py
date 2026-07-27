from tkinter import ttk
import calculator as calc

def build_mot_tab(notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Motor")

    frame = ttk.Frame(tab)
    frame.pack(side="left", anchor="n", padx=20, pady=20)

    fields = [
        "Flow (gpm)",
        "Displacement (in³/rev)"
    ]

    entries = {}

    for field in fields:
        ttk.Label(frame, text=field).pack()
        entry = ttk.Entry(frame)
        entry.pack()
        entries[field] = entry

    output = ttk.Label(frame, text="", justify="left")
    output.pack()












    return tab
