import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import turtle

screen = turtle.Screen()
screen.bgcolor("white") 
t = turtle.Turtle()
t.speed(1)

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.height = height
        self.width = width
    
    def showdisk(self):
        print("Disk Name: ", self.name)
        print("Disk Position: ", self.xpos, self.ypos)
        print("Disk Height: ", self.height)
        print("Disk Width: ", self.width)
        t.penup()
        t.goto(self.xpos, self.ypos)
        t.pendown()
        t.begin_fill()
        t.forward(self.width/2)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width/2)
        t.end_fill()

    def newpos(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def cleardisk(self):
        t.penup()
        t.goto(self.xpos, self.ypos)
        t.pendown()
        t.color("white")
        t.begin_fill()
        t.forward(self.width/2)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width/2)
        t.end_fill()
        self.name = ""
        self.xpos = 0
        self.ypos = 0
        self.height = 0
        self.width = 0

def main():
    disk = Disk("d1", 0, 0, 20, 40)
    disk.showdisk()
    disk.cleardisk()
    turtle.mainloop()


if __name__ == "__main__":
    main()


