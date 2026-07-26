import tkinter as tk
import calculator as calc
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
info_frame = ttk.Frame(root)

info_frame.pack(side="left", anchor="n", pady= 20, padx=20)

root.title("Cylinder Calculator")
root.geometry("500x500")

fields = [
    "Bore (in)",
    "Rod (in)",
    "Stroke (in)",
    "Pressure (psi)",
    "Flow (gpm)"
]


entries = {}


for field in fields:
    tk.Label(info_frame, text=field).pack()
    entry = tk.Entry(info_frame)
    entry.pack()
    entries[field] = entry
   

output = tk.Label(info_frame, text="", justify="left")
output.pack()

def calculate():
    bore = float(entries["Bore (in)"].get())
    rod = float(entries["Rod (in)"].get())
    stroke = float(entries["Stroke (in)"].get())
    psi = float(entries["Pressure (psi)"].get())
    flow = float(entries["Flow (gpm)"].get())
    if rod > bore:
        messagebox.showerror("Invalid Input", "Rod diameter must be smaller " \
        "than bore diameter")
        entries["Rod (in)"].delete(0, 'end')
        entries["Rod (in)"].focus_set()
        return 

    push, pull = calc.force(psi, bore, rod)
    ext_speed, ret_speed = calc.speed(flow, bore, rod)
    ext_time, ret_time = calc.time(flow, stroke, bore, rod)

    text = (
        f"Push Force: {push:,.0f} lbs\n"
        f"Pull Force: {pull:,.0f} lbs\n\n"
        f"Extension Speed: {ext_speed:.0f} in/min\n"
        f"Retraction Speed: {ret_speed:.0f} in/min\n\n"
        f"Extension Time: {ext_time:.0f} sec\n"
        f"Retraction Time: {ret_time:.0f} sec"
    )

    output.config(text=text)

def reset_fields():
    entries["Bore (in)"].delete(0, 'end')
    entries["Rod (in)"].delete(0, 'end')
    entries["Stroke (in)"].delete(0, 'end')
    entries["Pressure (psi)"].delete(0, 'end')
    entries["Flow (gpm)"].delete(0, 'end')

    output.config(text="")
    entries["Bore (in)"].focus_set() 




tk.Button(info_frame, text="Calculate", command=calculate).pack()
tk.Button(info_frame, text="Reset", command=reset_fields).pack()

root.bind("<Return>", lambda event: calculate())
entries["Bore (in)"].focus_set()
root.mainloop()    
