import turtle
import random

def makeLine():
    my_pen.forward(50)
    my_pen.right(90)
    my_pen.forward(1)
    my_pen.right(90)
    my_pen.forward(50)
    my_pen.right(90)
    my_pen.forward(1)
    my_pen.right(90)

def writeBase(pos):
    if pos%2 == 0:
        my_pen.goto(-40, distanta - 7)
    else:
        my_pen.goto(60, distanta - 7)
    my_pen.down()
    my_pen.write(str(len(samples[pos])) + ' bp')
    my_pen.up()
    my_pen.goto(0, distanta)
    my_pen.down()

samples = []
distanta = 280

with open("Lab5/sequence.fasta", "r") as f:
    next(f)
    seq_original = f.read() #seq_original din fisier

seq_original = seq_original[0:1500] 
seq_original = seq_original.replace("\n", "") #secventa fara spatii

for i in range(0, 10):
    index_1 = random.randrange(0, 1380)
    index_2 = random.randrange(index_1 + 100, 1480)
    samples.append(seq_original[index_1:index_2])

samples.sort(key=len, reverse=True)

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("The migration of DNA segments on the electrophoresis gel")

my_pen = turtle.Turtle()

my_pen.color("grey")
my_pen.up()
my_pen.goto(0, distanta)
my_pen.down()

for i in range(2):
    my_pen.forward(50)
    my_pen.right(90)
    my_pen.forward(10)
    my_pen.right(90)

my_pen.color("white")

for i in samples:
    my_pen.up()
    
    dist_i = len(i)/10/2
    distanta -= dist_i

    my_pen.goto(0, distanta)
    writeBase(samples.index(i))
    makeLine()

my_pen.up()
my_pen.goto(500, 500)
wn.exitonclick()