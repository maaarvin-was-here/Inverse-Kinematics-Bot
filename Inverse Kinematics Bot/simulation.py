import tkinter as tk
import math
from segment import Segment #segment object params: length, starting_coords, angle, parent, child
from conversions import to_degrees, to_radians



class App(tk.Tk):

    sim = tk.Tk()

    sim.geometry('600x500')

    greeting = tk.Label(text="2D Robot Arm Simulation")
    greeting.pack(pady=(10,10))


    C = tk.Canvas(sim, width=550, height=430, highlightthickness=1, highlightbackground="black")
    C.pack()


    x_val = C.create_text((530, 10), text="X : -")
    y_val = C.create_text((530, 30), text="Y : -")

    def motion(event):
        x, y = event.x, event.y
        C.itemconfigure(x_val, text = "X: {}".format(x))
        C.itemconfigure(y_val, text = "Y: {}".format(430 - y))


    ## TODO: FIX ANGLE ERASING AND UPDATING 
    def callback(event):
        x, y = event.x, event.y
        print("Clicked at {}, {}".format(x, y))
        seg2.angle = (seg2.angle + 45) % 360
        end_x = seg2.length * math.cos(to_radians(seg2.angle))
        end_y = seg2.length * math.sin(to_radians(seg2.angle))
        seg2.coords = (seg2.start[0], 430 - seg2.start[1], end_x, end_y)


    def draw_seg(seg):
        # arm1 = C.create_line(seg.start[0], 430 - seg.start[1], seg.end[0], 430 - seg.end[1])
        end_x = seg.length * math.cos(to_radians(seg.angle))
        end_y = seg.length * math.sin(to_radians(seg.angle))
        print(end_x, end_y)
        arm1 = C.create_line(seg.start[0], 430 - seg.start[1], end_x, end_y)
        return arm1

    seg1 = Segment(300, (0,0), 45, None, None)
    c_seg1 = draw_seg(seg1)

    seg2 = Segment(300, (seg1.end[0], seg1.end[1]), 45, seg1, None)
    c_seg2 = draw_seg(seg2)



    angle_between = 180 - seg1.angle + seg2.angle
    angle_val = C.create_text((530, 50), text="A: {}".format(angle_between))

    '''
    IK Math


    seg1.end = seg2.start


    '''


    
    def quit(event=None):
        sim.destroy()

    sim.bind('<Escape>', quit)
    C.bind('<Motion>', motion)
    C.bind('<Button-1>', callback)


app = App()
app.mainloop()