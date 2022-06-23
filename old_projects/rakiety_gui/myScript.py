from random import randint
from rocket import Rocket
from time import sleep
from PIL import ImageTk, Image
import tkinter as tk



root = tk.Tk()

list_of_rocket_images = ["rocket1.png", "rocket2.png",
                         "rocket3.png", "rocket4.png", "rocket5.png"]
my_img_list = [ImageTk.PhotoImage(Image.open(element))
               for element in list_of_rocket_images]
labels = [tk.Label(root, image=my_img_list[i])
          for i in range(len(my_img_list))]
rockets = [Rocket(speed=randint(1,5)) for _ in range(1,5)]

def startRace():
    k = 0.05
    for label in labels:
        label.place(relx=k, rely=0.87)
        k += 0.2
    for i in range(len(rockets)+1):
        rockets[i].moveUp
        rockets[i].speed = randint(1,5)
        labels[i].place(rely=float(labels[i].place_info()[
                            'rely']) - rockets[i].speed*0.0308)

def nextMove():
    for i in range(len(rockets)):
        if float(labels[i].place_info()['rely']) <= 0.1:
                print("The winner is:", rockets[i].id)
                return
        else:        
            rockets[i].moveUp
            rockets[i].speed = randint(1,5)
            labels[i].place(rely=float(labels[i].place_info()[
                                'rely']) - rockets[i].speed*0.0308)

    

list_of_rocket_images = ["rocket1.png", "rocket2.png",
                         "rocket3.png", "rocket4.png", "rocket5.png"]

my_img_list = [ImageTk.PhotoImage(Image.open(element))
               for element in list_of_rocket_images]


canvas = tk.Canvas(root, height=800, width=800, bg='green')
canvas.pack()

frame1 = tk.Frame(root, bg='red')
frame1.place(relheight=0.1, relwidth=1)


labels = [tk.Label(root, image=my_img_list[i])
          for i in range(len(my_img_list))]

i = 0.05
for label in labels:
    label.place(relx=i, rely=0.87)
    i += 0.2

start = tk.Button(root, text='START', padx=5, pady=10,
                  bg='#856ff8', command=startRace)
move_up_button = tk.Button(frame1, text='Next Move', padx=5, pady=10, bg='#856ff8', command=nextMove)
move_up_button.place(x=730)

start.pack()
root.mainloop()
