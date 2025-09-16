from turtle import*
speed(-1)
side = 6
for i in range(side):
    for i in range (side):
        for i in range(side):
            fd(25)
            lt(360/side)
            dot(2)
        fd(50)
        lt(360/side)  #360/5
    fd(100)
    lt(360/side)
hideturtle()
mainloop()       