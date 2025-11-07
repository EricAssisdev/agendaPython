from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Contato
from .forms import ContatoForm

def home(request):
    """View principal - redireciona para lista de contatos"""
    return redirect('lista_contatos')

def lista_contatos(request):
    """Lista todos os contatos com busca e filtros"""
    contatos_list = Contato.objects.all()
    
    # Busca
    query = request.GET.get('q', '')
    if query:
        contatos_list = contatos_list.filter(
            Q(nome__icontains=query) |
            Q(email__icontains=query) |
            Q(telefone__icontains=query) |
            Q(celular__icontains=query) |
            Q(empresa__icontains=query)
        )
    
    # Filtro por categoria
    categoria = request.GET.get('categoria', '')
    if categoria:
        contatos_list = contatos_list.filter(categoria=categoria)
    
    # Filtro por favoritos
    favoritos = request.GET.get('favoritos', '')
    if favoritos == '1':
        contatos_list = contatos_list.filter(favorito=True)
    
    # Paginação
    paginator = Paginator(contatos_list, 12)  # 12 contatos por página
    page_number = request.GET.get('page')
    contatos = paginator.get_page(page_number)
    
    context = {
        'contatos': contatos,
        'query': query,
        'categoria_selecionada': categoria,
        'favoritos': favoritos,
        'total_contatos': Contato.objects.count(),
        'total_favoritos': Contato.objects.filter(favorito=True).count(),
    }
    
    return render(request, 'contatos/lista_contatos.html', context)

def detalhes_contato(request, pk):
    """Exibe detalhes de um contato específico"""
    contato = get_object_or_404(Contato, pk=pk)
    return render(request, 'contatos/detalhes_contato.html', {'contato': contato})

def criar_contato(request):
    """Cria um novo contato"""
    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES)
        if form.is_valid():
            contato = form.save()
            messages.success(request, f'Contato "{contato.nome}" criado com sucesso!')
            return redirect('detalhes_contato', pk=contato.pk)
    else:
        form = ContatoForm()
    
    return render(request, 'contatos/form_contato.html', {
        'form': form,
        'titulo': 'Novo Contato',
        'botao': 'Criar Contato'
    })

def editar_contato(request, pk):
    """Edita um contato existente"""
    contato = get_object_or_404(Contato, pk=pk)
    
    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES, instance=contato)
        if form.is_valid():
            contato = form.save()
            messages.success(request, f'Contato "{contato.nome}" atualizado com sucesso!')
            return redirect('detalhes_contato', pk=contato.pk)
    else:
        form = ContatoForm(instance=contato)
    
    return render(request, 'contatos/form_contato.html', {
        'form': form,
        'contato': contato,
        'titulo': 'Editar Contato',
        'botao': 'Salvar Alterações'
    })

def deletar_contato(request, pk):
    """Deleta um contato"""
    contato = get_object_or_404(Contato, pk=pk)
    
    if request.method == 'POST':
        nome = contato.nome
        contato.delete()
        messages.success(request, f'Contato "{nome}" excluído com sucesso!')
        return redirect('lista_contatos')
    
    return render(request, 'contatos/deletar_contato.html', {'contato': contato})

def toggle_favorito(request, pk):
    """Alterna o status de favorito de um contato"""
    contato = get_object_or_404(Contato, pk=pk)
    contato.favorito = not contato.favorito
    contato.save()
    
    if contato.favorito:
        messages.success(request, f'"{contato.nome}" adicionado aos favoritos!')
    else:
        messages.info(request, f'"{contato.nome}" removido dos favoritos.')
    
    # Redireciona para a página anterior
    next_url = request.GET.get('next', 'lista_contatos')
    return redirect(next_url)
