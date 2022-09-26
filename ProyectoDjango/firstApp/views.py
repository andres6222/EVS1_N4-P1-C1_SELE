from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def display(response):
    return HttpResponse(
        "<h1>Hola</h1><p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Suscipit quas quae totam enim dolores molestiae illo aperiam voluptatibus, <br> possimus omnis explicabo sapiente, at, eum sint perspiciatis fugit officiis unde necessitatibus?</p><form action=""><input type='text' placeholder='Ingresa texto'><button>Nada</button></form>")