from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import VagaEmprego
from .forms import VagaEmpregoForm
from django.contrib.auth.decorators import login_required

@login_required
def listar_vagas(request):
    vagas = VagaEmprego.objects.all()
    return render(request, 'vaga/index.html', {'vagas': vagas})

@login_required
def criar_vaga(request):
    if request.method == 'POST':
        form = VagaEmpregoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaga cadastrada com sucesso!')
            return redirect('listar_vagas')  # Sem o namespace
    else:
        form = VagaEmpregoForm()
    return render(request, 'vaga/form_vaga.html', {'form': form, 'titulo': 'Cadastrar Vaga'})

@login_required
def editar_vaga(request, pk):
    vaga = get_object_or_404(VagaEmprego, pk=pk)
    if request.method == 'POST':
        form = VagaEmpregoForm(request.POST, request.FILES, instance=vaga)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaga atualizada com sucesso!')
            return redirect('listar_vagas')  # Sem o namespace
    else:
        form = VagaEmpregoForm(instance=vaga)
    return render(request, 'vaga/form_vaga.html', {'form': form, 'titulo': 'Editar Vaga'})

@login_required
def deletar_vaga(request, pk):
    vaga = get_object_or_404(VagaEmprego, pk=pk)
    if request.method == 'POST':
        vaga.delete()
        messages.success(request, 'Vaga deletada com sucesso!')
        return redirect('listar_vagas')  # Sem o namespace
    return render(request, 'vaga/confirmar_delete.html', {'vaga': vaga})