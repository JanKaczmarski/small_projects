import tkinter as tk
from tkinter import Button
from math import sqrt

root = tk.Tk()

def countArea():
    for i in buttons1:
        buttons1[i].destroy()

    #Rectangle boxy
    def createRectangleEntryBoxes():
        for i in buttons2:
            buttons2[i].destroy()
        global entry_list
        entry_list = [tk.Entry(root) for _ in range(2)]
        entry_canvas_list = [canvas.create_window(200*(i+1),140,window=entry_list[i]) for i in range(len(entry_list))]
        lables_list=[tk.Label(canvas,fg='red' , text='wporwadź długość boku') for _ in range(len(entry_list))]
        lables_list_packed=[lables_list[i].place(x=200*(i)+139, y=100) for i in range(len(lables_list))]
        get_area = tk.Button(canvas, text='get_area', pady=15, padx=10, fg='white', bg='purple', command=countRectangleArea)
        get_area.place(x=300, y=600)

    #Pitagoras boxy
    def createPitagorasEntryBoxes():
        for i in buttons2:
            buttons2[i].destroy()
        global entry_list
        entry_list = [tk.Entry(root) for _ in range(2)]
        entry_canvas_list = [canvas.create_window(200*(i+1),140,window=entry_list[i]) for i in range(len(entry_list))]
        lables_list=[tk.Label(canvas,fg='red' , text='wporwadź długość boku') for _ in range(len(entry_list))]
        lables_list_packed=[lables_list[i].place(x=200*(i)+139, y=100) for i in range(len(lables_list))]
        get_area = tk.Button(canvas, text='get_area', pady=15, padx=10, fg='white', bg='purple', command=countPitagoras)
        get_area.place(x=300, y=600)

    #Triangle boxy
    def createTriangleEntryBoxes():
        for i in buttons2:
            buttons2[i].destroy()
        global entry_list
        entry_list = [tk.Entry(root) for _ in range(2)]
        entry_canvas_list = [canvas.create_window(200*(i+1),140,window=entry_list[i]) for i in range(len(entry_list))]
        label1 = tk.Label(canvas, fg='red', text='Wprowadź długość podstawy')
        label1.place(x=139, y=100)
        label2 = tk.Label(canvas, fg='red', text='Wprowadź wysokość')
        label2.place(x=339, y=100)
        get_area = tk.Button(canvas, text='get_area', pady=15, padx=10, fg='white', bg='purple', command=countTriangleArea)
        get_area.place(x=300, y=600)

    #Rectangle Area
    def countRectangleArea(): 
        x = float(entry_list[0].get())
        y = float(entry_list[1].get())
        label = tk.Label(root, text=x*y)
        canvas.create_window(300, 230, window=label, height=40, width=60)    

    #Pitagoras
    def countPitagoras():
        x = float(entry_list[0].get())
        y = float(entry_list[1].get())
        label = tk.Label(root, text=round(sqrt(x**2 + y**2), 2))
        canvas.create_window(300, 230, window=label, height=40, width=60)

    #Triangle area    
    def countTriangleArea():
        x = float(entry_list[0].get())
        h = float(entry_list[1].get())
        label = tk.Label(root, text=(x*h)/2)
        canvas.create_window(300, 230, window=label, height=40, width=60)  

    pitagoras = Button(root, text='Przeciwprostokątna', padx=10, pady=10, bg='red', command=createPitagorasEntryBoxes)
    pitagoras.place(x=100, y=150)

    rectangle = Button(root, text='prostokąt', padx=10, pady=10, bg='red', command=createRectangleEntryBoxes)
    rectangle.place(x=310, y=150)

    triangle = Button(root, text='trójkąt', padx=10, pady=10, bg='red', command=createTriangleEntryBoxes)
    triangle.place(x=560, y=150)

    buttons2 = {'pitagoras':pitagoras, 'rectangle':rectangle, 'triangle':triangle}

def kalkulator():
    pass

def countCircuit():
    pass

class Rectangle():
    """Basicily rectangle"""
    def __init__(self, width:float, length:float):
        self.width= width
        self.length = length
    def countArea(self):
        return 
        
canvas = tk.Canvas(root, height=700, width=700, bg='grey')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relheight=0.05, relwidth=1, rely=0.95)

calculator = Button(frame, text='Kalkulator', padx=10, pady=5, fg='white', bg='purple', command=kalkulator)
calculator.pack()

area_counter = Button(frame, text='Pole figury', pady=5, padx=10, fg='white', bg='purple', command=countArea)
area_counter.place(x=100)

area_circuit = Button(frame, text='Obwód figury', pady=5, padx=10, fg='white', bg='purple', command=countCircuit)
area_circuit.place(x=500)

buttons1 = {'kalkulator':calculator,'obwód':area_circuit,'pole':area_counter}
root.mainloop()

#Aktualnie robie input boxy w myScript.py, chce zrobić interfejs w którym mozna wporwadzićdane liczbowe do programu