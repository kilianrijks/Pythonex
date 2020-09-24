import turtle
colors = [ "#F60000","#FF8C00","#FFEE00","#4DE94C","#3783FF","#4815AA"]
turtle.bgcolor("black")


for x in range(50):
    turtle.pencolor(colors[x % 6])
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(250)
    turtle.right(20)

turtle.done()
    
    
