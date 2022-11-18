# Importaciones
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Definición de variables: se le agregan atributos a la clase screen que le indican al pc el tamaño del espacio largo
# y acho, un color para el fondo de la ventana, un título a la ventana y una taza de refresco con la cuál se actualiza.

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
# Esto es para que reconozca los comandos que se ejecutan al presionar las teclas para movimiento.
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Se crea un ciclo para decirle al pc que el juego esté activo mientras la función "game_is_on" esté corriendo,
# para ello llaman tres atributos de tal función

game_is_on = True
while game_is_on:
    screen.update()

    time.sleep(0.1)
    snake.move()

    #Condición que detecta cuando la clase snake colisione con la clase food.
    if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

    #Condición que detecta cuando la clase snake colisione con la clase wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Ciclo que detecta cuando la clase snake colisione con la clase tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()













