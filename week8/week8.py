# def getGrade(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
#
# marks = [95, 90, 89.9, 80, 79.9, 70, 65, 60, 59.9, 0]
# for mark in marks:
#     print("Your grade is ", getGrade(mark))



# import turtle
#
# def choosecolor(height):
#     if height <=200:
#         return("red")
#     elif height <=100:
#         return("yellow")
#     else:
#         return("green")
#
# def drawbar(t, height, gap):
#     if height >= 0:
#     t.pendown()
#     t.fillcolor(choosecolor(height))
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
#
# def barchart(data):
#     maxheight = max(data)
#     minheight = min(data)
#     border = 10
#     bottom = min(minheight, 0) - border
#     num_bars = len(data)
#
#
#     gap = (maxheight + border) / 25
#
#
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right = 40 * num_bars + border
#     top = maxheight + 4 * border
#     wn.setworldcoordinates(-border, bottom, right, top)
#
#     t = turtle.Turtle()
#     t.color("blue")
#     t.fillcolor("red")
#     t.pensize(3)
#
#     for height in data:
#         drawbar(t, height, gap)
#
#
# data = [95, 72, 23, 240, 160, 185, 220]
# barchart(data)

import math
# def findHypot(a,b):
#     hypot = (a ** 2 + b ** 2) ** 0.5
#     return hypot
#
# def calcWithMath(a, b):
#     hypot = (a ** 2 + b ** 2) ** 0.5
#     return hypot
#
# print(calcWithMath(3,4))
# print(findHypot(3,4))

