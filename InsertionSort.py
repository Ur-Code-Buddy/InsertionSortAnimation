import turtle
import random
import time

delay_time = .5  #in seconds

screen = turtle.Screen()
screen.setup(800, 600)
screen.tracer(0, 0)
screen.title('Insertion Sort Animation')
turtle.speed(0)
turtle.hideturtle()

def draw_bar(x, y, w, h):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor('gray')
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.end_fill()

def draw_bars(v):
    x, w = -200, 500 / len(v)
    for i, h in enumerate(v):
        draw_bar(x, -200, w, h)
        x += w

def insertion_sort(v):
    for i in range(len(v)):
        j = i
        while j > 0 and v[j-1] > v[j]:
            v[j-1], v[j] = v[j], v[j-1]
            turtle.clear()
            draw_bars(v)
            screen.update()
            time.sleep(delay_time)
            j -= 1

v = [random.randint(1, 500) for _ in range(30)]

t1 = time.time()
insertion_sort(v)
t2 = time.time()
print('elapsed time =', t2-t1)

turtle.done()
