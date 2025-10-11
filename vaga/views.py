from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import VagaEmprego
from .forms import VagaEmpregoForm
from django.contrib.auth.decorators import login_required
from .forms import VagaEmpregoForm, VagaFiltroForm  # ← ADICIONE


@login_required
def listar_vagas(request):
    vagas = VagaEmprego.objects.all()
    # ========== ADICIONE ESTE BLOCO ==========
    # Criar instância do formulário
    filtro_form = VagaFiltroForm(request.GET or None)
    
    # Aplicar filtros se válido
    if filtro_form.is_valid():
        # Filtro por descrição
        descricao = filtro_form.cleaned_data.get('descricao')
        if descricao:
            vagas = vagas.filter(descricao__icontains=descricao)
        
        # Filtro por data início
        data_inicio = filtro_form.cleaned_data.get('data_inicio')
        if data_inicio:
            vagas = vagas.filter(data_cadastro__date__gte=data_inicio)
        
        # Filtro por data fim
        data_fim = filtro_form.cleaned_data.get('data_fim')
        if data_fim:
            vagas = vagas.filter(data_cadastro__date__lte=data_fim)
        
        # Filtro por status
        apenas_ativas = filtro_form.cleaned_data.get('apenas_ativas')
        if apenas_ativas:
            vagas = vagas.filter(ativo=True)

    return render(request, 'vaga/index.html', {
        'vagas': vagas,
        'filtro_form': filtro_form  # ← ADICIONE
    })

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