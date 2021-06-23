from django.shortcuts import render

# Create your views here.
def contacto(request):
  return render(request,'core/contactanos.html')

def productos(request):
  return render(request,'core/nuestrosproductos.html')

def home(request):
  return render(request,'core/pagina.html')

def informacion(request):
  return render(request,'core/quienesSomos.html')

def sismos(request):
  return render(request,'core/sismos.html')