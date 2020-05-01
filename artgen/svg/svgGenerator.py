import random
from . import robotGenerator

class svgGenerator:
    def __init__(self, canvasSize=(500,500)):
        self.canvasHeight = canvasSize[0]
        self.canvasWidth = canvasSize[1]
        self.header = '<svg height="{}" width="{}">'.format(self.canvasHeight, self.canvasWidth)
        self.footer = '</svg>'
        self.body = ''
        self.duration=5


    def addCircles(self, color, count):
        r = self.canvasHeight/100
        for c in range (1, count):
            cx = random.randint(0+r, self.canvasWidth-r)
            cy = random.randint(0+r, self.canvasHeight-r)
            self.addCircle(cx, cy, r, color, color)

    def addCircle(self, cx, cy, r, color1, color2, grow=False, pulseColor=''):
        stroke = ''
        if color1!=color2:
            stroke='stroke="#{}" stroke-width="4"'.format(color2)
        self.body += '<circle cx="{}" cy="{}" r={} {} fill="#{}" >'.format(cx, cy, r, stroke, color1)
        if grow:
            self.body+='<animate attributeName="r" values="{};{}" dur="{}" repeatCount="indefinite" />'.format(r/2, r*2, self.duration)
        self.body+='</circle>'


    def getSvg(self):
        return self.header + self.body + self.footer

    def getRobot(self, color1, color2):
        r = robotGenerator.robotGenerator((self.canvasHeight, self.canvasWidth))
        r.generateHead(1, self.canvasHeight/10, self.canvasHeight/8, (color1, color2))
        self.body+= r.robotSVG