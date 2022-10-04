#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
ladybug.penup()

#configure ladybug legs
num_legs = 6
leg_size = 80
leg_space = 75 / num_legs
n = 0
n2 = 0
ladybug.pensize(5)


#draw legs
ladybug.pendown()
while (n < num_legs):
    ladybug.goto(0, -50)
    ladybug.setheading(leg_space*n)
    ladybug.forward(leg_size)
    n = n + 2

leg_space = -75 / num_legs

while (n2 < num_legs):
    ladybug.goto(0,-35)
    ladybug.setheading(-leg_space*n2)
    ladybug.forward(-leg_size)
    n2 = n2 + 2


# and body
ladybug.penup()
ladybug.goto(15, -50) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(80)

# config dots
num_dots = 1
num_dots2 = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 1 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 10)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots = num_dots + 1

while (num_dots2 <= 1 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos + 20)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 30)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots2 = num_dots2 + 1

ladybug.penup()



  

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()