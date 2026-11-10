import turtle as t

wn = t.Screen()
wn.setup(width = 800, height = 600)

#t.circle(50)

circle_colors = ["lightblue", "lightgreen"]
circle_num = 0

#-------Make buttons-------
t.fillcolor("lightcoral")
t.penup()
t.goto(-275, -250)
t.pendown()
t.begin_fill()
t.circle(75)
t.end_fill()
for step in range (2):  
    t.fillcolor(circle_colors[circle_num])
    t.penup()
    t.forward(262.5)
    t.pendown()
    t.begin_fill()
    t.circle(75)
    t.end_fill()
    circle_num = circle_num + 1

#-----Make text------
t.


wn.mainloop()

