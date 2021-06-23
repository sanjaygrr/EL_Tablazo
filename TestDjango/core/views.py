from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request,'core/pagina.html')

def sismos(request):
  return render(request,'core/sismos.html')

def informacion(request):
  return render(request,'core/quienesSomos.html')

def productos(request):
  return render(request,'core/nuestrosproductos.html')

def contacto(request):
  return render(request,'core/contactanos.html')
