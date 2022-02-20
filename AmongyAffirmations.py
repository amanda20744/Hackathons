import turtle
import random

t = turtle.Turtle()
o = turtle.Turtle()
dot = turtle.Turtle()
pen = turtle.Turtle()
l = turtle.Turtle()
sketch = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.register_shape("amongus", ((0, 30), (-10, 30), (-15, 25), (-15, 15), (-20, 15), (-20, 0), (-20, -15), (-15, -15), (-15, -25), (-10, -25), (-5, -25), (-5, -15), (5, -15), (5, -25), (10, -25), (15, -25), (15, -15), (15, 0), (15, 5), (17.5, 8.75), (20, 12.5), (17.5, 16.25), (15, 20), (10, 25)))
screen.register_shape("oval", ((0, 10), (-5, 9.5), (-7.5, 7.5), (-12.5, 5), (-15, 0), (-12.5, -5), (-7.5, -7.5), (-5, -9.5), (0, -10), (5, -9.5), (7.5, -7.5), (12.5, -5), (15, 0), (12.5, 5), (7.5, 7.5), (5, 9.5)))
screen.register_shape("leaf", ((0,0), (2.5,0), (2.5,7.5), (7.5, 10), (10,15), (5,14), (1.25, 10), (-2.5,14), (-7.5,15), (-5, 10), (0,7.5)))
o.penup()
o.shape("oval")
o.color("#729fb3")
o.left(90)
o.goto(5, -60)
t.shape("amongus")
t.left(90)
t.color("#5f2f8f")
t.penup()
t.goto(0, -75)
dot.penup()
dot.color("white")
dot.shape("circle")
dot.shapesize(0.3,0.3,0.3)
dot.goto(10, -55)
l.penup()
l.shape("leaf")
l.left(90)
l.color("#1e6319")
l.goto(-5, -45)

def circle1():
    sketch.circle(random.randint(1, 3))


sketch.penup()
sketch.color("white")
for i in range(50):
    sketch.goto(random.randint(-250, 250), random.randint(-250, 250))
    sketch.begin_fill()
    circle1()
    sketch.end_fill()

sketch.color("#505a5e")
sketch.goto(-1000, -100)
sketch.begin_fill()
for i in range(2):
    sketch.forward(2000)
    sketch.right(90)
    sketch.forward(200)
    sketch.right(90)
sketch.end_fill()

screen.update()

affirmations = [
  "You're doing great babe!",
  "May all your wishes come true!",
  "Tomorrow is a new day.",
  "Sussy Baka",
  "I Love You",
  "Love yourself!",
  "I am grateful to have you.",
  "You are worthy."
  "You are worthy of good things.",
  "Do not compare yourself to others.",
  "Treat yourself today!",
  "You are enough.",
  "You look amazing!",
  "I love everything you do.",
  "Be proud of yourself",
  "Choose love today.",
  "The only approval you need is your own!",
  "You are a blessing!",
  "Never give up!",
  "Keep you head held high!",
  "You are limitless!",
  "Believe in yourself!",
  "You are loved!",
  "Don't be so hard on yourself.",
  "Have a great day today.",
  "Manifesting success for you!",
  "You're hot!"
]

pen.penup()
pen.color("white")

def space():
  pen.clear()
  rando = random.randint(0, len(affirmations) - 1)
  pen.write(affirmations[rando], align="center", font=("Verdana", 15, "normal"))

screen.onkey(space, 'space')
screen.listen()