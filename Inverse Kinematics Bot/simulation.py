import tkinter as tk
from segment import Segment #segment object params: length, starting_coords, angle, parent, child

print("this will be a simulation")

sim = tk.Tk()

sim.geometry('600x500')

greeting = tk.Label(text="2D Robot Arm Simulation")
greeting.pack(pady=(10,10))


C = tk.Canvas(sim, width=550, height=430, highlightthickness=1, highlightbackground="black")
C.pack()

# x_val = tk.Label(sim, text="X: -")
# y_val = tk.Label(sim, text="Y: -")
# x_val.pack()
# y_val.pack()

x_val = C.create_text((530, 10), text="X : -")
y_val = C.create_text((530, 30), text="Y : -")

def motion(event):
    x, y = event.x, event.y
    C.itemconfigure(x_val, text = "X: {}".format(x))
    C.itemconfigure(y_val, text = "Y: {}".format(430 - y))
    

def draw_seg(seg):
    arm1 = C.create_line(seg.start[0], 430 - seg.start[1], seg.end[0], 430 - seg.end[1])

seg1 = Segment(230, (0,0), 45, None, None)
draw_seg(seg1)

seg2 = Segment(230, (seg1.end[0], seg1.end[1]), 90, seg1, None)
draw_seg(seg2)

angle_between = 180 - seg1.angle + seg2.angle
angle_val = C.create_text((530, 50), text="A: {}".format(angle_between))




    
def quit(event=None):
    sim.destroy()

sim.bind('<Escape>', quit)
C.bind('<Motion>', motion)



sim.mainloop()