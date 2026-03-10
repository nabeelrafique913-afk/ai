from turtle import *
tracer(10)
bgcolor("black")
col = ('gold' , 'green')
for i in range(1000):
    pencolor(col[i%2])
forward(i*2)
right(121)
hideturtle()
done()    