
class robotGenerator:
    def __init__(self, canvasSize=(500,500)):
        self.canvasHeight = canvasSize[0]
        self.canvasWidth = canvasSize[1]
        self.robotSVG = ''

    def generateHead(self, style, ri, ro, colors):
        self.headCenter = (self.canvasWidth/2, self.canvasHeight/3)
        self.headInnerRadius = ri
        self.headOuterRadius = ro

        if style==1:
            headShape = '<rect x="{}" y="{}" width="{}" height="{}" fill="#{}">'.format(
                    int(self.headCenter[0]-self.headOuterRadius/2), 
                    int(self.headCenter[1]-self.headOuterRadius/2), 
                    int(self.headOuterRadius), 
                    int(self.headOuterRadius),
                    colors[0])
        
        self.robotSVG+= headShape   
        self.generateEyes(style, colors)
        self.robotSVG+= '</rect>' # close the rect.

    def generateEyes(self, style, colors):

        eyes = ''
        eyes += '<circle cx="{}" cy="{}" r={} fill="#{}" />'.format(5, 0, 5, "00")
        eyes += '<circle cx="{}" cy="{}" r={} fill="#{}" />'.format(5, 15, 5, "00")
        self.robotSVG +=eyes


    def generateMouth(self, style=1):
        pass

