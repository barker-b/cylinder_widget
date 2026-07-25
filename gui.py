import tkinter as tk
import calculator as calc
from tkinter import messagebox

root = tk.Tk()

root.title("Cylinder Calculator")
root.geometry("500x500")

tk.Label(root, text="Bore (in)").pack()
bore_entry = tk.Entry(root)
bore_entry.pack()

tk.Label(root, text="Rod (in)").pack()
rod_entry = tk.Entry(root)
rod_entry.pack()

tk.Label(root, text="Stroke (in)").pack()
stroke_entry = tk.Entry(root)
stroke_entry.pack()

tk.Label(root, text="Pressure (psi)").pack()
psi_entry = tk.Entry(root)
psi_entry.pack()

tk.Label(root, text="Flow (gpm)").pack()
flow_entry = tk.Entry(root)
flow_entry.pack()


output = tk.Label(root, text="", justify="left")
output.pack()

def calculate():
    bore = float(bore_entry.get())
    rod = float(rod_entry.get())
    stroke = float(stroke_entry.get())
    psi = float(psi_entry.get())
    flow = float(flow_entry.get())
    if rod > bore:
        messagebox.showerror("Invalid Input", "Rod diameter must be smaller " \
        "than bore diameter")
        rod_entry.delete(0, 'end')
        rod_entry.focus_set()
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
    bore_entry.delete(0, 'end')
    rod_entry.delete(0, 'end')
    psi_entry.delete(0, 'end')
    flow_entry.delete(0, 'end')
    stroke_entry.delete(0, 'end')

    output.config(text="")
    bore_entry.focus_set() 




tk.Button(root, text="Calculate", command=calculate).pack()
tk.Button(root, text="Reset", command=reset_fields).pack()

root.bind("<Return>", lambda event: calculate())
bore_entry.focus_set()
root.mainloop()    
