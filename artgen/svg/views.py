from django.http import HttpResponse
from .svgGenerator import svgGenerator


def index(request):
    svg = svgGenerator.basic()
    return HttpResponse(svg)