from tkinter import ttk
import calculator as calc
import cylinder_tab as cyl

def build_mot_tab(notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Motor")

    frame = ttk.Frame(tab)
    frame.pack(side="left", anchor="n", padx=20, pady=20)

    fields = [
        "Flow (gpm)",
        "Displacement (in³/rev)",
        "Pressure (psi)",
    ]

    entries = {}

    for field in fields:
        ttk.Label(frame, text=field).pack()
        entry = ttk.Entry(frame)
        entry.pack()
        entries[field] = entry

    output = ttk.Label(frame, text="", justify="left")
    output.pack()

    def calculate():
        flow = float(entries["Flow (gpm)"].get())
        displacement = float(entries["Displacement (in³/rev)"].get())
        pressure = float(entries["Pressure (psi)"].get())

        speed = calc.mot_speed(flow, displacement)
        torque = calc.torque(pressure, displacement)
        
        # text lines still need formatting.
        text =(
            f"Motor speed is {speed} rpm's.\n"
            f"Motor torque is {torque} in-lb's"
        )

        output.configure(text=text)
    

    def reset_fields():
        entries["Flow (gpm)"].delete(0, 'end')
        entries["Displacement (in³/rev)"].delete(0, 'end')
        entries["Pressure (psi)"].delete(0, 'end')

        output.config(text="")
        entries["Flow (gpm)"].focus_set()
        pass

    ttk.Button(frame, text="Calculate", command=calculate).pack()
    ttk.Button(frame, text="Reset", command=reset_fields).pack()











    return tab
