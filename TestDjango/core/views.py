from django.shortcuts import render

# Create your views here.
def pagina(request):
  return render(request,'core/pagina.html')

