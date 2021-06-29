from django.http import request
from django.shortcuts import render
from .models import Cliente
from .forms import CLiente_form


# Create your views here.
def contacto(request):
  return render(request,'core/contactanos.html')

def productos(request):
  return render(request,'core/nuestrosproductos.html')

def pagina(request):
  return render(request,'core/pagina.html')

def informacion(request):
  return render(request,'core/quienesSomos.html')

def sismos(request):
  return render(request,'core/sismos.html')

def cliente(request):
    client = Cliente.objects.all()
    datos = {
      "client": client
    }
    return render(request,'core/clientes.html',datos)
  #  return render(request,'core/clientes.html')


def form_cliente(request):
    data = { 
     'form': CLiente_form()
    }

    if request.method == 'POST':
      formulario = CLiente_form(data=request.POST)
      if formulario.is_valid():
         formulario.save()
         data["mensaje"] = "Guardado Correctamente"
      else:
         data["form"] = formulario

    return render(request,'core/cliente_formulario.html', data)
  # return render(request,'core/cliente_formulario.html')