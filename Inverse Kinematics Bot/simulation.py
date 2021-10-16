import tkinter as tk

print("this will be a simulation")

sim = tk.Tk()

sim.geometry('600x500')

greeting = tk.Label(text="2D Robot Arm Simulation")
greeting.pack(pady=(10,10))


can = tk.Canvas(sim, width=550, height=430, highlightthickness=1, highlightbackground="black")
can.pack()

# x_val = tk.Label(sim, text="X: -")
# y_val = tk.Label(sim, text="Y: -")
# x_val.pack()
# y_val.pack()

x_val = can.create_text((530, 10), text="X : -")
y_val = can.create_text((530, 30), text="Y : -")

def motion(event):
    x, y = event.x, event.y
    can.itemconfigure(x_val, text = "X: {}".format(x))
    can.itemconfigure(y_val, text = "Y: {}".format(y))
    
    






    
def quit(event=None):
    sim.destroy()

sim.bind('<Escape>', quit)
can.bind('<Motion>', motion)



sim.mainloop()