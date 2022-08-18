import turtle
import random


s= turtle.Screen()
s.title("Juego: Tortuguitas")
s.bgcolor("orange")


t1= turtle.Turtle()
t1.hideturtle()
t1.shape("turtle")
t1.shapesize(2,2,2)
t1.color("white" , "black")
t1.pensize(5)

t2= turtle.Turtle()
t2.hideturtle()
t2.shape("turtle")
t2.shapesize(2,2,2)
t2.color("black" , "white")
t2.pensize(5)

t1.penup()
t1.goto(200,200)
t1.pendown()
for i in range(4):
    t1.forward(100)
    t1.right(90)

t1.penup()
t1.goto(-200, 150)
t1.showturtle()


t2.penup()
t2.goto(200,-200)
t2.pendown()
for i in range(4):
    t2.forward(100)
    t2.left(90)

t2.penup()
t2.goto(-200, -150)
t2.showturtle()


dado = [1,2,3,4,5,6]
for i in range(20):
    if t1.pos() >= (200,200):
        print("La tortuga negra ha ganado!!")
        break
    elif t2.pos() >= (200,-200):
        print("La tortuga blanca ha ganado!!")
        break
    else:
        turno1 = input("Presiona la tecla enter para avanzar la tortuga negra")
        turno1 = random.choice(dado)
        print("Tu numero es:", turno1, "\n Avanzas: ",turno1*20)
        t1.pendown()
        t1.forward(20*turno1)

        turno2 = input("Presiona la tecla enter para avanzar la tortuga blanca")
        turno2 = random.choice(dado)
        print("Tu numero es:", turno2, "\n Avanzas: ",turno2*20)
        t2.pendown()
        t2.forward(20*turno2)

    
turtle.done()


















