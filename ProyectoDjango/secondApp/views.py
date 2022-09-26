from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def display(response):
    return HttpResponse("<img src='' alt='no carga la imagen'><ul><li>1</li><li>2</li><li>3</li><li>4</li></ul><a href='https://portales.inacap.cl/'>Inacap</a><h2>Probando texto en <i>Cursiva</i></h2><h3>probando texto en <u>subrayado</u></h3>")