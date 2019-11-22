from django.shortcuts import render, redirect

# Create your views here.
from cor.forms import ClienteForm
from cor.models import Cliente


def coreHome(request):
    if (request.method == 'POST'):
        cliente = ClienteForm(request.POST)
        if (cliente.is_valid()):
            cadastro = cliente.save(commit=False)
            cadastro.save()
        return redirect('/')
    else:
        cliente = ClienteForm()
    return render(request, 'cor/cadastrarCliente.html', {'ClienteForm': cliente})


def listaCliente(request):
    clientes = Cliente.objects.values()
    return render(request,'cor/listaCliente.html', {'Clientes': clientes})