from django.shortcuts import redirect, render
from core.forms import ProveedoresForm
from .models import Proveedor


# Create your views here.
def pagina(request):
    return render(request, 'core/pagina.html')


def contacto(request):
    return render(request, 'core/contactanos.html')


def quienesSomos(request):
    return render(request, 'core/quienesSomos.html')


def nuestrosproductos(request):
    return render(request, 'core/nuestrosproductos.html')




# Create your views here.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        super().__init__()


def listado(request):
    proveedores = Proveedor.objects.all()
    datos = {"proveedores": proveedores}
    return render(request, 'core/listado.html', datos)


def form_proveedores(request):
    datos = {'form': ProveedoresForm()}

    if request.method == 'POST':
        formulario = ProveedoresForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/form_proveedor.html', datos)


def form_mod_proveedor(request, id):
    # El id es el identificador de la tabla proveedores
    # Buscamos los datos en la base de datos
    # Buscamos con el id que llega desde la url

    proveedor = Proveedor.objects.get(Identificacion=id)

    datos = {'form': ProveedoresForm(instance=proveedor)}

    if request.method == 'POST':
        formulario = ProveedoresForm(request.POST, instance=proveedor)
        if formulario.is_valid:
            formulario.save()
            datos['form'] = formulario
            datos['mensaje'] = "Modificados correctamente"

    return render(request, 'core/form_mod_proveedor.html', datos)


def form_del_proveedor(request, id):

    proveedor = Proveedor.objects.get(Identificacion=id)

    proveedor.delete()

    return redirect(to="listado")
