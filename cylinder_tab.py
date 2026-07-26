import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import calculator as calc

def build_cyl_tab(notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Cylinder")

    frame_1 = ttk.Frame(tab)
    frame_1.pack(side="left", anchor="n", padx=20, pady=20)

    frame_2 = ttk.Frame(tab)
    frame_2.pack(side="left", anchor="n", padx=20, pady=20)



    fields_1 = [
        "Bore (in)",
        "Rod (in)",
        "Stroke (in)",
        "Pressure (psi)",
        "Flow (gpm)"
    ]


    fields_2 = [
        "Desired speed (in/min)"
    ]


    entries_1 = {}
    entries_2 = {}


    for field in fields_1:
        ttk.Label(frame_1, text=field).pack()
        entry = ttk.Entry(frame_1)
        entry.pack()
        entries_1[field] = entry


    for field in fields_2:
        ttk.Label(frame_2, text=field).pack()
        entry = ttk.Entry(frame_2)
        entry.pack()
        entries_2[field] = entry
    


    output_1 = ttk.Label(frame_1, text="", justify="left")
    output_1.pack()


    output_2 = ttk.Label(frame_2, text="", justify="left")
    output_2.pack()

    def calculate():
        bore = float(entries_1["Bore (in)"].get())
        rod = float(entries_1["Rod (in)"].get())
        stroke = float(entries_1["Stroke (in)"].get())
        psi = float(entries_1["Pressure (psi)"].get())
        flow = float(entries_1["Flow (gpm)"].get())
        if rod > bore:
            messagebox.showerror("Invalid Input", "Rod diameter must be smaller "\
            "than bore diameter")
            entries_1["Rod (in)"].delete(0, 'end')
            entries_1["Rod (in)"].focus_set()
            return 

        push, pull = calc.force(psi, bore, rod)
        ext_speed, ret_speed = calc.speed(flow, bore, rod)
        ext_time, ret_time = calc.time(flow, stroke, bore, rod)

        text_1 = (
            f"Push Force: {push:,.0f} lbs\n"
            f"Pull Force: {pull:,.0f} lbs\n\n"
            f"Extension Speed: {ext_speed:.0f} in/min\n"
            f"Retraction Speed: {ret_speed:.0f} in/min\n\n"
            f"Extension Time: {ext_time:.0f} sec\n"
            f"Retraction Time: {ret_time:.0f} sec"
        )

        output_1.config(text=text_1)

        

    def reset_fields():
        entries_1["Bore (in)"].delete(0, 'end')
        entries_1["Rod (in)"].delete(0, 'end')
        entries_1["Stroke (in)"].delete(0, 'end')
        entries_1["Pressure (psi)"].delete(0, 'end')
        entries_1["Flow (gpm)"].delete(0, 'end')

        output_1.config(text="")
        entries_1["Bore (in)"].focus_set() 


    def speed_calculate():
        des_speed = float(entries_2["Desired speed (in/min)"].get())
        bore = float(entries_1["Bore (in)"].get())
        flow = calc.desired_speed(des_speed, bore)

        text_2 = (
            f"Needed flow for {des_speed:.0f} in/min.\n"
            f"{flow:.1f} gpm."
        )

        output_2.config(text=text_2)

    ttk.Button(frame_1, text="Calculate", command=calculate).pack()
    ttk.Button(frame_1, text="Reset", command=reset_fields).pack()
    ttk.Button(frame_2, text="Calculate\nFlow", command=speed_calculate).pack()
    
    return tab
