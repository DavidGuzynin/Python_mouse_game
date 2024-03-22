from tkinter import *

def display_coordinates (Event):
    my_label['text']='flag coordinates:'f'x={Event.x} y={Event.y}'
    global photoimage
    photoimage=PhotoImage(file='red-golf-flag-pole-with-marks-and-wind-direction-vector-24910597.png')
    global myimage
    myimage=my_canvas.create_image(Event.x,Event.y,image=photoimage)
my_window = Tk()
my_window.title('Python_mouse_game')
my_canvas = Canvas (my_window,width=400,height=400, background='green')
my_label=Label (bd=4, relief="solid", font="Arial 22", bg="Red", fg="grey")
my_canvas.bind('<Button-1>', display_coordinates)
my_canvas.grid(row=0,column=0)
my_label.grid(row=1,column=0)
photoimage=PhotoImage(file='red-golf-flag-pole-with-marks-and-wind-direction-vector-24910597.png')
myimage=my_canvas.create_image(200,200,image=photoimage)
my_window.mainloop()