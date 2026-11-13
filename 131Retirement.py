import turtle as t
import random
from playsound3 import playsound

rbutton = t.Turtle()
bbutton = t.Turtle()
gbutton = t.Turtle()
conbutton = t.Turtle()
cookbutton = t.Turtle()
mesbutton = t.Turtle()
cookie = t.Turtle()

writer = t.Turtle()
painter = t.Turtle()
index = 0
wn = t.Screen()
wn.setup(width = 800, height = 600)
writer.hideturtle()
painter.hideturtle()
conbutton.hideturtle()
mesbutton.hideturtle()
cookbutton.hideturtle()
cookie.hideturtle()
cookie_clicked = False

messages = ["Have a good day!", "You are looking dapper today!", "Have a relaxing day!", "Sending smiles your way!", "You're thought of and appreciated!", "Here's a note to brighten your day!"]
random.shuffle(messages)
message = messages[0]
random_color = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "coral", "cornflowerblue", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", "grey", "honeydew", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"]
cookies = ["1bitecookie.gif", "2bitecookie.gif"]

#-------Make buttons-------
rbutton.shape("circle")
rbutton.color("black", "lightcoral")
bbutton.shape("circle")
bbutton.color("black", "lightblue")
gbutton.shape("circle")
gbutton.color("black", "lightgreen")
conbutton.shape("circle")
conbutton.color("black", "hotpink")
mesbutton.shape("circle")
mesbutton.color("black", "yellow")
cookbutton.shape("circle")
cookbutton.color("black", "brown")


rbutton.shapesize(stretch_wid=8, stretch_len=8)
rbutton.speed(0)
bbutton.shapesize(stretch_wid=8, stretch_len=8)
bbutton.speed(0)
gbutton.shapesize(stretch_wid=8, stretch_len=8)
gbutton.speed(0)
conbutton.shapesize(stretch_wid=8, stretch_len=8)
conbutton.speed(0)
mesbutton.shapesize(stretch_wid=8, stretch_len=8)
mesbutton.speed(0)
cookbutton.shapesize(stretch_wid=8, stretch_len=8)
cookbutton.speed(0)

rbutton.penup()
rbutton.goto(-275, -185)
bbutton.penup()
bbutton.goto(0, -185)
gbutton.penup()
gbutton.goto(275, -185)
conbutton.penup()
conbutton.goto(-275, -185)
mesbutton.penup()
mesbutton.goto(0, -185)
cookbutton.penup()
cookbutton.goto(275, -185)


#-----Make homescreen text------
font_setup = ("Arial", 40, "normal")
writer.speed(0)
writer.penup()
writer.goto(-190,50)
writer.write("Click One Button", font = font_setup)


#-------clear screen and add background on button click---------
def red_clicked(x,y):
    writer.clear()
    rbutton.hideturtle()
    gbutton.hideturtle()
    bbutton.hideturtle()
    painter.penup()
    painter.goto(-400,300)
    painter.pencolor("lightcoral")
    painter.fillcolor("lightcoral")
    painter.begin_fill()
    painter.speed(0)
    for step in range(2):
            painter.forward(800)
            painter.right(90)
            painter.forward(600)
            painter.right(90)
    painter.end_fill()
    conbutton.showturtle()
    mesbutton.showturtle()
    cookbutton.showturtle()
    writer.write("Click One Button", font = font_setup)

def green_clicked(x,y):
    writer.clear()
    rbutton.hideturtle()
    gbutton.hideturtle()
    bbutton.hideturtle()
    painter.penup()
    painter.goto(-400,300)
    painter.pencolor("lightgreen")
    painter.fillcolor("lightgreen")
    painter.begin_fill()
    painter.speed(0)
    for step in range(2):
            painter.forward(800)
            painter.right(90)
            painter.forward(600)
            painter.right(90)
    painter.end_fill()
    conbutton.showturtle()
    mesbutton.showturtle()
    cookbutton.showturtle()
    writer.write("Click One Button", font = font_setup)

def blue_clicked(x,y):
    writer.clear()
    rbutton.hideturtle()
    gbutton.hideturtle()
    bbutton.hideturtle()
    painter.penup()
    painter.goto(-400,300)
    painter.pencolor("lightblue")
    painter.fillcolor("lightblue")
    painter.begin_fill()
    painter.speed(0)
    for step in range(2):
            painter.forward(800)
            painter.right(90)
            painter.forward(600)
            painter.right(90)
    painter.end_fill()
    conbutton.showturtle()
    mesbutton.showturtle()
    cookbutton.showturtle()
    writer.write("Click One Button", font = font_setup)


rbutton.onclick(red_clicked)
bbutton.onclick(blue_clicked)
gbutton.onclick(green_clicked)

def conclicked(x,y):
    writer.clear()
    painter.pensize(5)
    painter.speed(0)
    conbutton.hideturtle()
    cookbutton.hideturtle()
    mesbutton.hideturtle()
    playsound("confetti.mp3")
    for sprinkle in range(100):
        x_position = random.randint(-400,400)
        y_position = random.randint(-300, 300)
        painter.penup()
        painter.teleport(int(x_position), int(y_position))
        painter.setheading(random.randint(0, 360))
        painter.pencolor(random.choice(random_color))
        painter.pensize(3)
        painter.pendown()
        painter.forward(10)
    playsound("trumpet.mp3")
    painter.pensize(1)
    painter.speed(5)

def mesclicked(x,y):
      writer.clear()
      conbutton.hideturtle()
      mesbutton.hideturtle()
      cookbutton.hideturtle()
      writer.goto(-240,0)
      writer.write(f"{message}", font= ("Arial", 30, "normal"))
      playsound("cheering.mp3")


index = 0
def fcookie_oneclick(x,y):
    global index
    if (index == 2):
         cookie.hideturtle()
         playsound("eating.mp3")
         return
    wn.addshape(cookies[index])
    cookie.shape(cookies[index])
    playsound("eating.mp3")
    index += 1
    index = min(2, index)

      
def cookclicked(x,y):
      writer.clear()
      conbutton.hideturtle()
      mesbutton.hideturtle()
      cookbutton.hideturtle()
      cookie.goto(0,0)
      wn.addshape("full_cookie.gif")
      cookie.shape("full_cookie.gif")
      cookie.showturtle()
      cookie.onclick(fcookie_oneclick)


conbutton.onclick(conclicked)
mesbutton.onclick(mesclicked)
cookbutton.onclick(cookclicked)




wn.mainloop()

