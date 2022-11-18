# Importación
from turtle import Turtle

ALIGNMENT = "center"  # Esto es para centrar el texto.
FONT = ("Courier", 24, "normal")  # Esto es para determinar la fuente de estilo de texto.


# Se crea la clase Score board
class Scoreboard(Turtle):

    # Se crea una función que define los parámetros de la clase que son: score, color, límite de escritura,
    # ubicación inicial y límite de escritura, esconder caracteres, y actualizar.

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # Función para actualizar la barra de puntaje con el centrado y la fuente.

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Función para que muestre un texto que es game over.

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # Función para que el sistema reconozca cuando se obtenga un punto y ejecute la actualización de la scoreboard.

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
