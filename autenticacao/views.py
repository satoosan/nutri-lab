from django.shortcuts import render
from django.http import HttpResponse
from .utils import password_is_valid
from django.shortcuts import redirect

# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')
        return HttpResponse(f'Testando') 
    
def logar(request):
    return render(request, 'login.html')