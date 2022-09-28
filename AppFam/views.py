from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppFam.models import Familia

# Create your views here.

def familia(request):

  familiar1 = Familia(nombre="Carlos", apellido="López", parentesco="Padre", altura=1.70, cumpleanios="1959-1-3")
  familiar1.save()

  familiar2 = Familia(nombre="Daniela", apellido="Tancredi", parentesco="Madre", altura=1.57, cumpleanios="1971-3-17")
  familiar2.save()

  familiar3 = Familia(nombre="Ignacio", apellido="López Tancredi", parentesco="Hermano", altura=1.71, cumpleanios="2001-10-14")
  familiar3.save()

  familiares = {"familiar1": familiar1, "familiar2": familiar2, "familiar3": familiar3}
  
  plantilla = loader.get_template("AppFam/index.html")
  documento = plantilla.render(familiares)

  return HttpResponse(documento)