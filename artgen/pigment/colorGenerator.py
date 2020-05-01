import random
import csv

class colorGenerator:
    def __init__(self):
        self.colors = []
        f_input =  open('./lib/colors/colornames_abridged.csv', 'r', newline='')
        self.colors = []
        for color in csv.DictReader(f_input):
            self.colors.append(color)

    def getColor(self):

        return random.choice(self.colors)['hexcode']

    def getColorWithName(self):
        color = random.choice(self.colors)
        return (color['hexcode'],color['name'])

    def getPalette(self, colorCount=10, method='default'):
        
        palette = []
        if method=='default':
            for x in range(1, colorCount):
                color = random.choice(self.colors)
                palette.append((color[hexcode],color[name]))
        
        return palette