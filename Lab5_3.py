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






class Hanoi(object):
    def __init__(self,n = 3, start = "A", workspace = "B", destination = "C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d" + str(i), 0, i * 150, 20, (n-1) * 30))
        
    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n-1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n-1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)

h = Hanoi()
h.solve()