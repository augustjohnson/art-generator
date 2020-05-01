from django.http import HttpResponse
from .svgGenerator import svgGenerator
from verbiage.verbiageGenerator import verbiageGenerator
from pigment.colorGenerator import colorGenerator


def index(request):
    
    svg = svgGenerator()
    vg = verbiageGenerator()
    name = vg.getAdjective().strip() + ' ' + vg.getNoun().strip()
    c = colorGenerator()
    color1 = c.getColorWithName()
    color2 = c.getColor()
    color3 = c.getColor()
    description = 'This work of art is entitled "{}" and is a representation of a color commonly known as "{}".'.format(name, color1[1])
    svg.addCircles(str(000000), 50)
    #svg.addCircle(250, 250, 100, color1[0], color2, grow=True)
    svg.getRobot(color1[0], color2)
    art = svg.getSvg()
    page = art + '<br><p>' + description + '</p>'
    return HttpResponse(page)