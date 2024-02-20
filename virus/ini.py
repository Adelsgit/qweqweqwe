import turtle
import math

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("white")

# Создание объекта черепахи
virus = turtle.Turtle()
virus.speed(0)  # Максимальная скорость рисования

# Функция для рисования круга с разными радиусами и цветами
def draw_circle(color, radius, x, y):
    virus.penup()
    virus.color(color)
    virus.goto(x, y)
    virus.pendown()
    virus.circle(radius)

# Функция для рисования "шипов"
def draw_spike(length, angle):
    virus.penup()
    virus.goto(0,0)
    virus.pendown()
    virus.forward(length)
    virus.right(angle)
    virus.forward(length / 2)
    virus.right(120)
    virus.forward(length / 2)
    virus.right(angle)
    virus.forward(length)
    virus.right(180 - angle)

# Основной круг
draw_circle("darkgreen", 60, 0, -60)

# Рисуем внешние "шипы"
for _ in range(12):
    draw_spike(100, 60)
    virus.right(30)  # Поворот на 30 градусов для следующего "шипа"

# Рисуем внутренние "шипы" меньшего размера
for _ in range(12):
    draw_spike(50, 60)
    virus.right(30)  # Поворот на 30 градусов для следующего маленького "шипа"

# Добавляем дополнительные детали в центр
for _ in range(6):
    draw_circle("red", 10, 0, -50)
    virus.right(60)

virus.hideturtle()  # Скрываем черепаху после завершения рисования

# Завершение работы с Turtle
turtle.done()
