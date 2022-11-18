
# Importaciones:

from turtle import Turtle
import random

# Creación de la clase de los puntos con las siguientes propiedades:
"""
shape es la forma, va en círculo
penup es para dejar de escribir la forma
shapesize es el tamaño del círculo
color para el color
velocidad de aparición: muy rápido
Actualizarse para que vuelva a aparecer.
función refresh:
Puede aparecer en una ubicación aleatoria entre el tamaño determinado del eje x, y.
"""

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)