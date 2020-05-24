import turtle as t
from itertools import cycle

colors = cycle(['red', 'yellow', 'orange', 'blue', 'purple', 'green', 'hot pink'])

def d_circle(size):
    t.pencolor(next(colors))
    t.circle(size)
    d_circle(size + 5)

t.bgcolor('black')
t.speed('fast')
t.pensize(4)
d_circle(30)




