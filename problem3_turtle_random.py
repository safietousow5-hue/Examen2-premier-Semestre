import turtle
import random
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
N = int(input("Entrez le nombre de formes a dessiner (0 a 9) : "))
def dessinerCarre(taille):
    for i in range(4):
        t.forward(taille)
        t.right(90)

def dessinerTriangle(taille):
    for i in range(3):
        t.forward(taille)
        t.left(120)

def dessinerCercle(taille):
    t.circle(taille)

for i in range (N):
    forme = random.randint(0, 2)
    taille = random.randint(20, 100)
    couleurs = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
    couleur = random.choice(couleurs)
    t.color(couleur)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)

    t.penup()
    t.goto(x, y)
    t.pendown()


    if forme == 0:
        dessinerCarre(taille)
    elif forme == 1:
        dessinerTriangle(taille)
    else:
        dessinerCercle(taille)

