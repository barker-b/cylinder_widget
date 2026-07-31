from tkinter import ttk
import calculator as calc
import cylinder_tab as cyl

def build_mot_tab(notebook):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Motor")

    frame_1 = ttk.Frame(tab)
    frame_1.pack(side="left", anchor="n", padx=20, pady=20)

    frame_2 = ttk.Frame(tab)
    frame_2.pack(side="left", anchor="n", padx=20, pady=20)

    fields_1 = [
        "Flow (gpm)",
        "Displacement (in³/rev)",
        "Pressure (psi)",
    ]

    fields_2 = [
        "Desired motor speed (rpm)",
    ]
    
    entries = {}

    for field in fields_1:
        ttk.Label(frame_1, text=field).pack()
        entry = ttk.Entry(frame_1)
        entry.pack()
        entries[field] = entry

    for field in fields_2:
        ttk.Label(frame_2, text=field).pack()
        entry = ttk.Entry(frame_2)
        entry.pack()
        entries[field] = entry
        
    output_1 = ttk.Label(frame_1, text="", justify="left")
    output_1.pack()

    output_2 = ttk.Label(frame_2, text="", justify="left")
    output_2.pack()
    
    def calculate():
        flow = float(entries["Flow (gpm)"].get())
        displacement = float(entries["Displacement (in³/rev)"].get())
        pressure = float(entries["Pressure (psi)"].get())

        speed = calc.mot_speed(flow, displacement)
        torque = calc.torque(pressure, displacement)
        
        
        # text lines still need formatting.
        text_1 = (
            f"Motor speed is {speed} rpm.\n"
            f"Motor torque is {torque} in-lb's"
        )

        
        output_1.configure(text=text_1)
        

    def speed_calculate():
        des_speed = float(entries["Desired motor speed (rpm)"].get())
        displacement = float(entries["Displacement (in³/rev)"].get())

        need_flow = calc.desired_motor_speed(des_speed, displacement)

        text_2 = (
            f"Flow for desired motor speed: {need_flow} gpm."
        )

        output_2.configure(text=text_2)
        
    def reset_fields():
        entries["Flow (gpm)"].delete(0, 'end')
        entries["Displacement (in³/rev)"].delete(0, 'end')
        entries["Pressure (psi)"].delete(0, 'end')

        output_1.config(text="")
        entries["Flow (gpm)"].focus_set()
        pass

    ttk.Button(frame_1, text="Calculate", command=calculate).pack()
    ttk.Button(frame_1, text="Reset", command=reset_fields).pack()
    ttk.Button(frame_2, text= "Calculate", command=speed_calculate).pack()











    return tab
