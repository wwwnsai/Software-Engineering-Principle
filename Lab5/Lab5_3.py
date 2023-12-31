import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import turtle

screen = turtle.Screen()
screen.bgcolor("white") 
t = turtle.Turtle()
t.speed(10)

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
        t.pencolor("black")
        t.penup()
        t.goto(self.xpos-self.width/2 - 20, self.ypos)
        t.pendown()
        t.write(self.name)
        t.penup()
        t.goto(self.xpos, self.ypos)
        t.pendown()
        t.forward(self.width/2)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width/2)

    def newpos(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def cleardisk(self):
        t.penup()
        t.goto(self.xpos, self.ypos)
        t.pendown()
        t.pencolor("white")
        t.goto(self.xpos-self.width/2 - 20, self.ypos)
        t.pendown()
        t.write(self.name)
        t.penup()
        t.goto(self.xpos, self.ypos)
        t.pendown()
        t.forward(self.width/2)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width/2)



class Pole(object):
    def __init__(self,name="", xpos=0,ypos=0,thick=10,length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length
        
    def showpole(self):
        t.penup()
        t.goto(self.pxpos,self.pypos)
        t.right(90)
        t.forward(15)
        t.write(self.pname)
        t.back(15)
        t.left(90)

        t.pendown()
        t.forward(self.pthick/2)
        t.left(90)
        t.forward(self.plength)
        t.left(90)
        t.forward(self.pthick)
        t.left(90)
        t.forward(self.plength)
        t.left(90)
        t.forward(self.pthick/2)
        
    def pushdisk(self, disk):
        self.stack.append(disk)
        disk.newpos(self.pxpos, self.toppos)
        disk.showdisk()
        self.toppos += disk.height

    def popdisk(self):
        disk = self.stack.pop()
        disk.cleardisk()
        self.toppos -= disk.height
        # disk.showdisk()
        return disk

     


class Hanoi(object):
    def __init__(self,n = 3, start = "A", workspace = "B", destination = "C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d" + str(i), 0, (i) * 150, 20, (n-i) * 30))

        
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